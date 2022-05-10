import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is not None:
            item = self.head
            self.head = self.head.next
            return item.value

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.
