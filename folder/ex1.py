class Animal:
    animal_type = 'Any animal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return "Hi, I am {} {} and I am {} !".format(self.animal_type, self.name, self.age)


class Dolphin(Animal):
    animal_type = "Dolphin"


class Zebra(Animal):
    animal_type = "Zebra"


d = Dolphin(age=20, name="Chuck")
z = Zebra("Zelda", 30)

print(d.say())
print(z.say())

