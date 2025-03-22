import random
from clases.player import Player
from clases.villain import Villian

def main():
    name_player = input("Welcome to the dungeon travel!, Please insert your name ")
    player = Player(name_player)

    villains = [Villian("Alien",50,10),
               Villian("Monster",50,10),
               Villian("Robot",50,10),
               ]
    
    print("The adventure begings!")

    while True :
        actual_villian = random.choise(villains)
        print(f"You find an enemy! it is the terrible {actual_villian.name}")

        while actual_villian.health > 0 :
            action = input ("What are going to do?(atack/run)").lower()

            if action == "attack":
                player_attack = player.attack()
                print("You hace attacked {actual_villian.name} and you caused {player_attack} of damage")
                actual_villian.recieve_damage(player_attack)

                if actual_villian > 0 :
                    villian_attack = actual_villian.attack()
                    print(f"{actual_villian.name} attacked you and caused {villian_attack} of damage")
                    player.recieve_damage(villian_attack)
            elif action == "run" :
                print("you decide to run")
                break
