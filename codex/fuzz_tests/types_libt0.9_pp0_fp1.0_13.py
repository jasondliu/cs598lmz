import types
types.FunctionType

def x():
    pass

print(x)
print(type(x))
print(type(x) is types.FunctionType)  # True

names = ['A', 'B', 'C']
print(names)
print(type(names))
names[1]
print(type(names[1]))
names[1] = 'D'
print(names)
print(type(names))

print(dir(types))

# isinstance
print('isinstance')
print(isinstance(x, types.FunctionType))  # True
print(isinstance(names, types.ListType))  # False
print(isinstance(names, list))  # True

print(type(isinstance))

print('type')
print(type(x))
a = str('hello')
print(type(a))
print(type(a) is type('hello'))  # True

print('types')
print(type(a) == type('hello'))
print(type(a) is str)
print(type(a) == str)
