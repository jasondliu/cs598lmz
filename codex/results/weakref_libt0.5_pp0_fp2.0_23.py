import weakref

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return "Node(%r)" % self.data

    def __del__(self):
        print "Deleting node: %r" % self.data

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "LinkedList(%r)" % self.head

    def __del__(self):
        print "Deleting list: %r" % self.head

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove(self
