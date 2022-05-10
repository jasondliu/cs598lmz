import gc, weakref

class Graph:
    def __init__(self, name):
        self.name = name
        self.next = None
    def set_next(self, next):
        print('%s.set_next(%s)' % (self.name, next.name))
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

print

print(len(gc.get_referrers(one)))
print(len(gc.get_referrers(two)))
print(len(gc.get_referrers(three)))
print(one)
print(two)
print(three)

class Graph:
    def __init__(self, name):
        self.name = name
        self.next
