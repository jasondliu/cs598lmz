import threading
threading.stack_size(2**27)

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.last = None
        temp = self.first
        self.first = self.first.next
        self.length -= 1
        return temp.value

    def isEmpty(self):
        return self.length == 0


class Stack():

