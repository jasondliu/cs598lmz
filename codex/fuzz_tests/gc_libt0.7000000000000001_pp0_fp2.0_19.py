import gc, weakref

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next

class List(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            tail = self.tail
            tail.next = node
            self.tail = node
    def pop(self):
        head = self.head
        if head is None:
            raise IndexError
        self.head = head.next
        return head.value

class Cycle(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            tail = self.tail
            tail.next = node
