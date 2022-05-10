import weakref
# Test weakref.ref()

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

def reverse_list(head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev

def reverse_list_recursive(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse_list_recursive_2(head, prev=None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list_recursive_2(next, head)

def reverse_list_recursive_
