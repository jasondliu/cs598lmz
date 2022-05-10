import gc, weakref
import pprint

class Graph:
    def __init__(self, name):
        self.name = name
        self.next = None
    def set_next(self, next):
        print('Linking nodes %s.next = %s' % (self, next))
        self.next = next
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)

# Construct a graph cycle
one = Graph('one')
two = Graph('two')
three = Graph('three')
one.set_next(two)
two.set_next(three)
three.set_next(one)

print()
print('three:', three)
for i in range(2):
    print('  referring objects:', [o() for o in gc.get_referents(three)])
    print('  gc.garbage:', gc.garbage)
    print()

print('Collecting')
n = gc.collect()
print('Unreachable objects
