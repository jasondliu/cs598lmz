from types import FunctionType
list(FunctionType(lambda x: x+1, {}, "", (), None))

# Test dict.items(), dict.keys(), dict.values()
print(dict(a=1, b=2, c=3).items())
print(dict(a=1, b=2, c=3).keys())
print(dict(a=1, b=2, c=3).values())

# Test dict.__setitem__
d = dict(a=1)
d['b'] = 2
print(d)

# Test dict.__getitem__
print(d['a'])

# Test dict.__delitem__
del d['a']
print(d)

# Test dict.__contains__
print(d)
print('b' in d)

# Test dict.__sizeof__
print(d)
print(sys.getsizeof(d))

# Test dict.__repr__
print(repr(d))

# Test dict.__iadd__
d += {'c': 3}
print(d)

# Test dict.__
