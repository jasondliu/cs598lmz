from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__())


a = [1]
print(type(a.__getitem__))
print(type(a.__getitem__(0)))


a = {'1':1}
print(type(a.__getitem__))
print(type(a.__getitem__('1')))

print(dir(int))
print(dir(FunctionType))
print(dir(int.__add__))


print(dir(abs))
print(dir(int.__radd__))

# print(dir(str))
a = str
print(a.__getitem__)

def test(a):
    print(a())

# from operator import itemgetter
def itemgetter(lst):
    return iter(lst)

a = itemgetter(['a','b'])
test(a.__getitem__)

a = itemgetter(['a','b'])
test(a().__next__)
