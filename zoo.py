class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
    

class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Miau!"
    
class Fish(Animal):
    def speak(self):
        return "Blub!"
    
class Bird(Animal):
    def speak(self):
        return "Tweet!"



if __name__ == "__main__":
    animals = [Dog("Burek"), Cat("Mruczek"), Bird("Tweety"), Fish("Nemo")]
    for a in animals:
        print(f"{a.name}: {a.speak()}")

