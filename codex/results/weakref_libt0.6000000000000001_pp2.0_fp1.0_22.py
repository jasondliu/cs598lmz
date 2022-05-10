import weakref


class LinkedList(object):
    """
    LinkedList
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __getitem__(self, index):
        if index < 0:
            index = self.length + index
        if index >= self.length:
            raise IndexError("LinkedList index out of range")
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def __str__(self):
        return '[' + ', '.join(str(item) for item in self) + ']'

    def __repr__(self):
        return 'LinkedList(' + str(self) + ')'

    def append(self, data):
        node = LinkedListNode(data)
        self
