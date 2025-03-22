
import random

class Villian :
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health       
        self.damge = damage

    def attack(self):
        return random.randint(5,15) 
    
    def recieve_damage(self, damage):
        self.health -= damage
        if (self.health) <= 0:
            print(f"{self.name} has been defeated")
            return True
        return False

    
    