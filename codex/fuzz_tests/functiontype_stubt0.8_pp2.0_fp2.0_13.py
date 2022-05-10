from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(isinstance(a, object))
print(type(FunctionType))
print(type(type))
print(type(object))
print(isinstance(FunctionType, object))
print(isinstance(type, object))
print(isinstance(object, object))

# names bound in inner scope can't be accessed in outer scope
# x = 'global x'
#
# def test():
#     x = 'local x'
#     print(x)
#
# test()
# print(x)

x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

# accessing global x from local scope is possible
x = 'global x'

def test():
    print(x)

test()
print(
