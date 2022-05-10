import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# Write a program to test gc.collect()
#
# The program should create a list of objects and add
# items to the list.
#
# The program should delete a few of the items in the list
# and then call gc.collect()
#
# The program should show that gc.collect() deletes items
# from the list that are not referenced.

# Write your program here
#random numbers between 1-10
import random

#create list of objects
class ExampleClass(object):
    
    def __init__(self):
        self.x = random.randint(1,10)
        
    def __del__(self):
        print("Deleting object")
        print("__del__ ran")
        
    def __repr__(self):
        return str(self.x)
    
    
    
    
objects = []

for i in range(0,10):
    objects.append(ExampleClass())
    
#delete a few objects
del objects[0]
del objects[0]


print("before collect
