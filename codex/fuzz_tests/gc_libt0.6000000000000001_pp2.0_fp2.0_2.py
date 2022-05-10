import gc, weakref

class Node:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __reversed__(self):
        current = self.tail
        while current:
            yield current.value
            current = current.prev

    def add_to_tail(self, value):
        if self.head is None:
            self.head = self.tail = Node(value, None, None)
        else:
            self.tail.next = Node(value, self.tail, None)
            self.tail = self.tail.next
        self._size += 1

    def add_to_head(self
