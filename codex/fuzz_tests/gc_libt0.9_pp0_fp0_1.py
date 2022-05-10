import gc, weakref
import sys

class my_class:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, ": Bye bye~")

class my_second_class:
    def __init__(self):
        self.my_o = my_class("my_o")

    def __del__(self):
        print("my_second_class: Bye bye~")
        
def A():
    x = my_second_class()
    x.my_o = None

def B():
    x = my_second_class()
    x = None

A()
B()
gc.collect()
print("Finished.")
