class Robot:

    def __init__(self, name, color, weight):  # Constructor function like in JS
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot("John", "red", 40)
r2 = Robot("Chris", "Blue", 30)

r1.introduce_self()
r2.introduce_self()
