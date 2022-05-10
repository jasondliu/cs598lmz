import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def findIntersection(head1, head2):
    #  Your Code Here
    l1 = length(head1)
    l2 = length(head2)
    if l1 > l2:
        for i in range(l1 - l2):
            head1 = head1.next
    elif l2 > l1:
        for i in range(l2 - l1):
            head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1 == head2:
            return head1.data

