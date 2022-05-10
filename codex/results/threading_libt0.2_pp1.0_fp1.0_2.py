import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('inpy.txt', 'r')
sys.stdout = open('outpy.txt', 'w')
from math import *
from collections import *
from queue import PriorityQueue
from heapq import heapify, heappop, heappush

def printGrid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()
    print()

def findUnassignedLocation(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

def usedInRow(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def usedInCol(arr, col,
