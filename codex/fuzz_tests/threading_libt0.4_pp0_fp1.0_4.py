import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from queue import PriorityQueue
from bisect import bisect_left, bisect_right


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(tree, arr, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    tree[mid] = Node(arr[mid])
    buildTree(tree, arr, start, mid - 1)
    buildTree(tree, arr, mid + 1, end)


def preorder(tree, arr, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    print(tree[mid].data, end=' ')
    preorder(tree, arr, start, mid
