from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2])
c = (x for x in [])
print(any(a))
print(any(b))
print(any(c))
print()

d = [1, 2, 3, 4, 5]
print(any(d))
print()

e = []
print(any(e))
print()

print(any('hello'))
print()

print(any(['hello', 'world']))
print(any(('hello', 'world')))
print()

print(any(iter([])))
print(any(iter([1, 2, 3])))
print()

# any can be called on an object of a class that implements __bool__ or __len__
class True_Class:
    def __bool__(self):
        return True
    def __len__(self):
        return 1

print(any(True_Class()))
print()

#any can be called on an object of a class that implements __iter__
class True_Class:
    def __iter__(self):
