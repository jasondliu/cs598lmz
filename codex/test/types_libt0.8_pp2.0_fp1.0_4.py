import types
types.MethodType(print,())

def f(self):
    return "Hello World!"

f.__get__(1)

class Demo:
    @staticmethod
    def f():
        return "Hello World!"

    @classmethod
    def f2(cls):
        return cls

Demo.f
Demo.f()
Demo.f2
Demo.f2()
