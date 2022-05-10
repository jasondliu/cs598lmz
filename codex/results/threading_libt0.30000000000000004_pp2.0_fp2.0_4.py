import threading
threading.stack_size(67108864)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

def reverse(head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

def merge(head_a, head_b):
    temp_a = head_a
    temp_b = head_b

    head_new = LinkedList()

    while(temp_a is not None and temp_b is not
