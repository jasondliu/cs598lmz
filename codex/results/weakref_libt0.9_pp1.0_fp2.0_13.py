import weakref

class Link(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = weakref.ref(tail)

    def dump(self):
        print self

    def __str__(self):
        return '{0.head} -> {0.tail}'.format(self)

    def __repr__(self):
        return 'Link({0.head}, {0.tail})'.format(self)

    def __getitem__(self, idx):
        return self if idx == 0 else self.tail[idx-1]

    def __gettail__(self):
        return self.tail()

# This code doesn't work, because the weak reference
# doesn't go through the __getitem__ method.
#
# instead, we should be using a wrapper function
# like __gettail__

a = Link('a', Link('b', Link('c', None)))
print a.tail
print a.tail.tail
print a.tail.tail.tail
print a[-1].tail[-1
