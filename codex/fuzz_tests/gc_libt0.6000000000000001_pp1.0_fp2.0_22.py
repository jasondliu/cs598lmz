import gc, weakref

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class F(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


def test_weakref_callback():
    f1 = F('1')
    f2 = F('2')
    f3 = F('3')
    f4 = F('4')
    f5 = F('5')
    f6 = F('6')
    f7 = F('7')
    f8 = F('8')
    f9 = F('9')

    f1.add_child(f2)
    f1.add_child(f3)
    f2.add_child(f4)
    f2.add_child(f5)
    f4.add_child(f6)
    f4.add_child(f7
