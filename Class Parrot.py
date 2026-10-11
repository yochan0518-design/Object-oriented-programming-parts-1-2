class Parrot:

    #class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the parrot class
blu = Parrot("blu", 10)
woo = Parrot("woo", 15)

# acess the class attributes
print("blu is a ()".format(blu.species))
print("woo is also a ()".format(woo.species))

#acess the instance attriutes
print("()is ()years old".format(blu.name, blu.age))
print("()is ()years old".format(woo.name, woo.age))