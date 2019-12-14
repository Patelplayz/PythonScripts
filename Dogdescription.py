
class Dog:

    def __init__(self, name, age, gender, noise):
        self.name = name
        self.age = age
        self.gender = gender
        self.noise = noise

    def show_profile(self):
        print("your dog " + self.name + " is " + self.age + " and is a " + self.gender)

    def bark(self):
        print(self.noise)

    def die(self):
        print(self.name + " is dead")


John =  Dog("John","5","Male", "woof")

John.show_profile()
John.bark()
John.die()