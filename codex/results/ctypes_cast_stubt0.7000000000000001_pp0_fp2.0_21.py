import ctypes
ctypes.cast(0xdeadbeef, ctypes.py_object)

# more dynamic and duck-typing
import collections
import datetime

# class Duck(object):
#     def quack(self):
#         print('Quaaack!')
#     def feathers(self):
#         print('The duck has white and gray feathers.')
# class Person(object):
#     def quack(self):
#         print("The person imitates a duck.")
#     def feathers(self):
#         print('The person takes a feather from the ground and shows it.')
# def in_the_forest(duck):
#     duck.quack()
#     duck.feathers()
#
# donald = Duck()
# john = Person()
# in_the_forest(donald)
# in_the_forest(john)

#
#
# class Flock(object):
#     def __init__(self):
#         self.flock = []
#     def add_duck(self, duck: Duck) -> None:
#         fly_method = get
