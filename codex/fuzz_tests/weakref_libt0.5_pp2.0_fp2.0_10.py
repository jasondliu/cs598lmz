import weakref


class Node(object):
    """
    Node of a linked list.

    :param value: value of the node
    :param prev: reference to the previous node
    :param next: reference to the next node
    """

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    """
    Linked list.

    :param iterable: iterable with values to be inserted into the list
    """

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next
