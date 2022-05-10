from types import FunctionType
a = (x for x in [1])
b = [1]
print(type(a))
print(type(b))
print(type(b) == type(a))
print(isinstance(b, type(a)))
print(isinstance(a, type(b)))
print(isinstance(b, list))
print(isinstance(a, list))
print(isinstance(type(b), type))
print(type(type(b)))
print(isinstance(FunctionType, type))
print(isinstance(type(a), FunctionType))
print(FunctionType == type)
print(type(lambda:None) == type)
print(type(type) == type)
print(type(type(lambda:None)) == type)
print(type(type(type)) == type)

class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        super().__init__()
        print('B')

class C(A):
    def __init__(self):
        super().__init__()
        print('
