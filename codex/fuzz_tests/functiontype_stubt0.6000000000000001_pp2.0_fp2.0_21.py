from types import FunctionType
a = (x for x in [1])
print(type(a))
a = [1]
print(type(a))

a = FunctionType
print(type(a))

a = lambda x: x
print(type(a))

a = uuid.uuid4()
print(type(a))

a = (1,)
print(type(a))

a = 1
print(type(a))

a = [1, 2, 3]
print(type(a))

a = {1:2, 3:4}
print(type(a))

a = "123"
print(type(a))

a = b"123"
print(type(a))

a = "123".encode("utf8")
print(type(a))

a = b"123".decode("utf8")
print(type(a))

a = b"123"
print(type(a))

a = "123".encode("utf8")
print(type(a))

a = 123
print(type(a))


class A(object):

