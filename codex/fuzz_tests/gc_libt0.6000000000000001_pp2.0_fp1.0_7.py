import gc, weakref
from pprint import pprint

class Graph(object):
    def __init__(self, name):
        self.name = name
        self.other = None
    def set_other(self, other):
        print('Connecting %s to %s' % (self, other))
        self.other = other
    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, self.name)

one = Graph('one')
two = Graph('two')
one.set_other(two)
two.set_other(one)

def show_backrefs(obj, level=0):
    print('%s%s' % (' ' * level * 2, obj))
    for referrer in gc.get_referrers(obj):
        show_backrefs(referrer, level + 1)

show_backrefs(one)
print()

# 清除引用链
one = two = None
show_backrefs(Graph)
