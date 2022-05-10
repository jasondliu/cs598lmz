from types import FunctionType
a = (x for x in [1])
ind = a.__reduce__()
print(ind[0])
print(ind[1])
print(ind[2])
print(ind[3])
b = ind[0](*ind[1])
print(b)
print(type(b))
print(ind[2])
c = ind[2]
print(type(c))


print("test 3-----------------------------------------")
class c:
    def __init__(self, a):
        self.a = a
        return
    def __reduce__(self):
        return (self.__setstate__,(666,))
    def __setstate__(self, x):
        self.a = x
        return
    def do_nothing(self):
        return

d = c(1)
e = d.__reduce__()
print(e[0])
print(e[1])
print(type(e[1]))

"""
test_ligo_sim():
  # reduction doesn't work correctly
  # on subclasses of actual classes,
  # which is a more realistic
