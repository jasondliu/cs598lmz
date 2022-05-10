import threading
threading.stack_size(67108864)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove(self, data):
        if self.head == None:
            return

        current = self.head
        prev = None

        if self.head.data == data:
            self.head = self.head.next

        while current != None:
            if current.data == data:
                prev.next = current.next
                break
            prev = current
            current = current.next

    def print(self):
        if self.head == None:
            return

        current = self.head
