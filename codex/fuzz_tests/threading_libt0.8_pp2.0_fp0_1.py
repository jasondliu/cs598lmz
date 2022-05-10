import threading
threading.stack_size(2**32)
sys.setrecursionlimit(2**32)

class Node:
    def __init__(self, data):
        self.data = data  # contains the data
        self.next = None  # contains the reference to the next node


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        if self.head is None:  # if stack is empty
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def pop(self):
        if self.head is None:  # if stack is empty
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        return temp.data

    def peek(self):
        if self.head is None:
            return -1
        return self.head
