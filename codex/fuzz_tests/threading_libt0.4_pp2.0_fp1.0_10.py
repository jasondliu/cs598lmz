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

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

class Solution:
    def __init__(self, head):
        self.head = head

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def insert(self, prev_node, data):
        if prev_node is None:
            print("
