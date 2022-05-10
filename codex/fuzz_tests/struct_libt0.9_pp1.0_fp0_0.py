import _struct


def ask_name():
    name = input("Name: ")
    return name


def ask_age():
    age = input("Age: ")
    return int(age)


def say_hello(name, age):
    print("Hello %s, your age is %d" % (name, age))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "name: %s, age: %d" % (self.name, self.age)

    def dump(self, f):
        string = self.__str__()
        f.write(string)
        f.write("\n")


def main
