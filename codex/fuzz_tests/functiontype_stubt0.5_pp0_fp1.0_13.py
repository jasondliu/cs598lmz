from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type((x for x in [1])))
print(type({x for x in [1]}))
print(type({x for x in [1]:x}))
print(type([]))
print(type({}))
print(type(()))
print(type(1))
print(type("1"))
print(type(FunctionType))
print(type(abs))
print(type(lambda x : x))
print(type(None))
print(type(1+1j))
print(type(False))
print(type(True))
print(type(Ellipsis))
print(type(x for x in [1]))
print(type(super))

# print(type(__import__("os")))

# print(type(__import__("os").path))

# print(type(__import__("os").path.dirname))

# print(type(__import__("os").path.dirname(__file__)))

# print(type(__import__("os").
