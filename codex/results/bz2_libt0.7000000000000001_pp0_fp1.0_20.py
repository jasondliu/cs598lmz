import bz2
bz2.compress("ahoj")

import time
time.sleep(1)
time.sleep(0.5)

import sys
sys.path.append('/home/tomas/')

import mymodule
mymodule.my_func()

import mymodule as my
my.my_func()

import __builtin__
print dir(__builtin__)

print type(mymodule)
print mymodule.my_func.__doc__
print my.my_func.__doc__

print my.__file__

# skoda je, ze neexistuje __print__


def my_decorator(func):
    def wrapper():
        print "before"
        func()
        print "after"
    return wrapper

def func():
    print "func"

# decorator
func = my_decorator(func)
func()

@my_decorator
def func():
    print "func"

func()

"""
def my_decorator(func):
    def wrapper():
        print "before"

