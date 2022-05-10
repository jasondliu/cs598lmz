import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from random import randint
import random

class Node:
    def __init__(self, nxt=None, val=0):
        self.next = nxt
        self.val = val

def create(head, n):
    if n == 0:
        return head
    head.next = create(Node(), n - 1)
    return head

def display_node(node):
    if node == None:
        print()
        return
    print(node.val, '->', end=' ')
    display_node(node.next)

def reverse(head):
    node = head
    if node == None:
        return None
    if node.next == None:
        return node
    else:
        rest = reverse(node.next)
        node.next.next = node
