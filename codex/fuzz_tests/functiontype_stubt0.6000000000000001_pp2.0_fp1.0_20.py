from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [1,2,3]
print(type(b))
c = "string"
print(type(c))
d = {"name":"bob"}
print(type(d))
e = [1,2,3,4,5]
print(type(e))
f = FunctionType
print(type(f))
g = {'name':'bob','age':20}
print(type(g))

print("-------------------------------")

print(type(123))
print(type("123"))
print(type([]))
print(type({}))
print(type(abs))

print("-------------------------------")

print(type(123) == type(456))
print(type("123") == type("456"))
print(type("123") == type(123))
print(type("123") == type([]))
print(type("123") == type(()))
print(type("123") == type({}))

print("-------------------------------")

a = type("123") == type("456")
print(a
