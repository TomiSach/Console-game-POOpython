import random
from clases.player import Player
from clases.villain import Villain

def main():
    name_player = input("Welcome to the dungeon travel! Please insert your name: ")
    player = Player(name_player)

    villains = [
        Villain("Alien", 50, 10),
        Villain("Monster", 50, 10),
        Villain("Robot", 50, 10),
    ]
    villains_defeated = []

    print("The adventure begins!")

    while villains:
        actual_villain = random.choice(villains)
        print(f"You find an enemy! It is the terrible {actual_villain.name}")

        while actual_villain.health > 0:
            action = input("What are you going to do? (attack/run)").lower()

            if action == "attack":
                player_attack = player.attack()
                print(f"You have attacked {actual_villain.name} and caused {player_attack} damage")
                actual_villain.receive_damage(player_attack)

                if actual_villain.health > 0:
                    villain_attack = actual_villain.attack()
                    print(f"{actual_villain.name} attacked you and caused {villain_attack} damage")
                    player.receive_damage(villain_attack)

            elif action == "run":
                print("You decided to run")
                break

            if player.health <= 0:
                print("Game over")
                return

            if actual_villain.health <= 0:
                villains_defeated.append(actual_villain)
                villains.remove(actual_villain)

            player.gain_experience(20)

        continuation = input("Do you want to continue? (y/n)").lower()
        if continuation != "y":
            print("Thank you for playing!")
            break

    print("Congrats, you defeated all the enemies!")

if __name__ == "__main__":
    main()