from types import FunctionType
a = (x for x in [1])
print(a, type(a))
for i in a:
    print(i)

def test():
    print(a)

test()

print(type(test))

# print(isinstance(test, FunctionType))


class Test:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("getter of x called")
        return self._x

    @x.setter
    def x(self, value):
        print("setter of x called")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter of x called")
        del self._x


def test_generator():
    print('enter test_generator')
    yield 1
    print('exit test_generator')


g = test_generator()
print(g.send(None))
try:
    g.send(None)
except StopIteration as e:
    print(
