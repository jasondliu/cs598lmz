from types import FunctionType
a = (x for x in [1])
is_generator_function(a)

b = {'k': 'v'}.keys()
is_generator_function(b)

c = [1, 2, 3]
is_generator_function(c)

d = {'k': 'v'}
is_generator_function(d)

e = 'a'
is_generator_function(e)

f = FunctionType
is_generator_function(f)

g = FunctionType(lambda x: 1 + x, globals(), 'lambda')
is_generator_function(g)

h = int
is_generator_function(h)


# in
class C:
    pass

def f():
    pass

class G(object):
    def __init__(self):
        self.x = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.x += 1
        if self.x > 10:
            raise StopIteration
        return self.x

g = G()


