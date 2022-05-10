fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

class A:
    pass

A.__dict__['__getattribute__'] = lambda self, name: 2
A().x

class A:
    def __init__(self):
        self.__dict__['x'] = 1

A().x

class A:
    pass

A.__getattribute__ = lambda self, name: 2
A().x

class A:
    def __getattribute__(self, name):
        return 2

A().x

class A:
    def __getattr__(self, name):
        return 2

A().x

class A:
    def __getattr__(self, name):
        return 2
    def __getattribute__(self, name):
        return 1

A().x

class A:
    def __getattr__(self, name):
        return 2
    def __getattribute__(self, name):
        return 1
    x = 3

A().x

a = 1
def f():
    a = 2

