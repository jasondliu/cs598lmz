fn = lambda: None
# Test fn.__code__.__eq__
print(fn.__code__ == fn.__code__)
# Test fn.__code__.__ne__
print(fn.__code__ != fn.__code__)
# Test fn.__code__.__lt__
print(fn.__code__ < fn.__code__)
# Test fn.__code__.__le__
print(fn.__code__ <= fn.__code__)
# Test fn.__code__.__gt__
print(fn.__code__ > fn.__code__)
# Test fn.__code__.__ge__
print(fn.__code__ >= fn.__code__)

# Test fn.__code__.__repr__
print(repr(fn.__code__))
# Test fn.__code__.__str__
print(str(fn.__code__))
# Test fn.__code__.__hash__
print(hash(fn.__code__))
print(hash(fn.__code__) == hash(fn.__code__))
print('-' * 20)



