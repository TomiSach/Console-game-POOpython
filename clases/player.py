import random

class Player :
    def __init__(self,name):
        self.name = name
        self.health = 100        
        self.level =1
        self.experience = 0

    def attack(self):
        return random.randint(10,20) * self.level
    
    def recieve_damage(self, damage):
        self.health -= damage
        if (self.health) <= 0:
            print(f"{self.nombre} has died. Game Over!")

    
    def gain_experience(self, experience):
        self.experience -= experience
        if (self.experience) >= 100:
            self.level += 1
            self.experience = 0
            print(f"{self.name} has leve up! to {self.level} level")