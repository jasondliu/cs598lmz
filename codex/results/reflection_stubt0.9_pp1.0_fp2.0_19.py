fn = lambda: None
gi = (i for i in ())
fn.__code__ = ()
getattr(gi, 'gi_code')()
a = 1
b = 2
assert a + b == 3
assert b + a == 3
def add(a, b):
    return a + b
assert add(a, b) == 3
assert add(b, a) == 3
class A(object):
  def add(self, a, b):
    return self.__add__(a, b)
  def __add__(self, a, b):
    return a + b
a = A()
assert a.add(a, b) == 3
assert a.add(b, a) == 3


class TestFor(object):
    def __init__(self, value, norm):
        self.value = value
        self.norm = norm

    def __iter__(self):
        self.x = 0
        while self.x < self.norm:
            yield self.value * self.x
            self.x += 1

    def extra(self):
        return str(self) + "foo"

for x in TestFor(value = 2
