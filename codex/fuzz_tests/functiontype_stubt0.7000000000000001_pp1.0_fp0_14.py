from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2, 3])

# print(a.__next__())

for i in a:
    print(i)

# print(a.__next__())
# print(a.__next__())


def add(a):
    def sum(b):
        return a + b
    return sum

a = add(1)
b = add(2)
print(a(2))
print(b(2))

print(type(a))

def deco(func):
    def in_deco(a, b):
        print("in deco")
        return func(a, b)
    return in_deco

@deco
def bar(a, b):
    print("in bar")
    return a + b

print(bar(1, 2))


# def deco(func):
#     def in_deco(*args, **kwargs):
#         print("in deco")
#         return func(*args, **kwargs)
#     return in_deco

