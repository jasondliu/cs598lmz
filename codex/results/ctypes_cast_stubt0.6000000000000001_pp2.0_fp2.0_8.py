import ctypes
ctypes.cast(addr, ctypes.py_object).value

def func():
    print('func')

func.__dict__

func.__dict__['key'] = 'value'

func.key

class Cls(object):
    def __init__(self):
        self.key = 'value'

cls = Cls()

cls.key

cls.__dict__

class Cls(object):
    def __init__(self):
        self.key = 'value'

cls = Cls()

cls.key

cls.__dict__

class Cls(object):
    def __init__(self):
        self.key = 'value'

cls = Cls()

cls.key

cls.__dict__

class Cls(object):
    def __init__(self):
        self.key = 'value'

cls = Cls()

cls.key

cls.__dict__

class Cls(object):
    def __init__(self
