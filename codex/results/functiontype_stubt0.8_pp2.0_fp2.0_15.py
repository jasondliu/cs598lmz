from types import FunctionType
a = (x for x in [1])

def aa():
    print(2)

ll = aa()

print(type(ll))
print(ll)

print(type(a) == GeneratorType)

print('-----------------')
print(type(aa) == FunctionType)
