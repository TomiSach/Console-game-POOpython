import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100        
        self.level = 1
        self.experience = 0

    def attack(self):
        return random.randint(10, 20) * self.level
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has died. Game Over!")
        else :
            print(f"{self.health} health points left")

    def gain_experience(self, experience):
        self.experience += experience
        if self.experience >= 100:
            self.level += 1
            self.experience = 0
            print(f"{self.name} has leveled up to level {self.level}!")

class Villain:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health       
        self.damage = damage

    def attack(self):
        return random.randint(5, 15)
    
    def receive_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated")
            return True
        return False