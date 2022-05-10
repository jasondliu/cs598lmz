from types import FunctionType
a = (x for x in [1])
print(isinstance(a,GeneratorType))
b = (x for x in [1])
print(isinstance(b,FunctionType))

def a():
    yield 1
print(isinstance(a,GeneratorType))
print(isinstance(a,FunctionType))

c = a()
print(isinstance(c,GeneratorType))
print(isinstance(c,FunctionType))

class A():
    def __iter__(self):
        return self
    def next(self):
        return 1

print(isinstance(A(),GeneratorType))
print(isinstance(A(),FunctionType))
print(isinstance(A().next(),GeneratorType))
print(isinstance(A().next(),FunctionType))

class B():
    def __iter__(self):
        return self
    def __next__(self):
        return 1

print(isinstance(B(),GeneratorType))
print(isinstance(B(),FunctionType))
print(isinstance(B().__next__(),GeneratorType))
print(isinstance(B().__
