from _struct import Struct
s = Struct.__new__(Struct)
s

# __new__ vs __init__

class A:
    def __new__(cls):
        print('A.__new__')
        return super().__new__(cls)
    
    def __init__(self):
        print('A.__init__')
A()

class B(A):
    def __new__(cls):
        print('B.__new__')
        return super().__new__(cls)
    
    def __init__(self):
        print('B.__init__')
B()

class B(A):
    def __new__(cls):
        print('B.__new__')
        return object.__new__(cls)
    
    def __init__(self):
        print('B.__init__')
B()

class B(A):
    pass
B()

# extending types

class Structure:
    _fields = []
