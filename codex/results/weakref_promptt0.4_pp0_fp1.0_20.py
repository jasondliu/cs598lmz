import weakref
# Test weakref.ref() on a function.
import sys
import gc


class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('MyClass.__del__')


def f():
    print('f()')


def callback(r):
    print(r)
    print(gc.collect())


def callback2(r):
    print(r)
    print(gc.collect())


def callback3(r):
    print(r)
    print(gc.collect())


def callback4(r):
    print(r)
    print(gc.collect())


def callback5(r):
    print(r)
    print(gc.collect())


def callback6(r):
    print(r)
    print(gc.collect())


def callback7(r):
    print(r)
    print(gc.collect())


def callback8(r):
    print(r)
    print(gc.collect())


def callback9(r):
    print(
