import weakref
# Test weakref.ref() with a callable object

def test(x, y):
    return 1

def test2(x, y):
    return 2

class Test(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(self):
        return 3

class Test2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __call__(self):
        return 4

tc = Test(1, 1)

w1 = weakref.ref(test)
w2 = weakref.ref(test2)
w3 = weakref.ref(tc)
w4 = weakref.ref(tc)

test(1, 1)
del test
test2(1, 2)
del test2
tc(1, 3)
del tc
