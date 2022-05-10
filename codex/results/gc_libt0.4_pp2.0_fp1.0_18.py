import gc, weakref
import sys

def f():
    print("f()")

def g():
    print("g()")

def h():
    print("h()")

class MyClass:
    def __init__(self, name):
        self.name = name
        self.callbacks = []
        self.refs = []

    def register(self, callback):
        self.callbacks.append(callback)
        self.refs.append(weakref.ref(callback))

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def unregister2(self, callback):
        ref = weakref.ref(callback)
        self.refs.remove(ref)

    def notify(self):
        for callback in self.callbacks:
            callback()

    def notify2(self):
        for ref in self.refs:
            callback = ref()
            if callback is not None:
                callback()
            else:
                print("removed")

    def __del__(self):
        print("MyClass.__del
