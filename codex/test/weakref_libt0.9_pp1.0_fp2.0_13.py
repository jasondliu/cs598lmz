import weakref

class Link(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = weakref.ref(tail)

