import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
from math import *
from collections import *
from queue import Queue
from heapq import heappush, heappop, heapify
 
my_file = open("input.txt", "r")
input = my_file.readline
 
 
def print_result(case_number, result):
    print("Case #{}: {}".format(case_number + 1, result))
 
 
def read_line():
    return list(map(int, input().strip().split()))
 
 
def read_int():
    return int(input())
 
 
def read_words():
    return input().split()
 
 
def read_integer_list():
    return list(map(int, input().split()))
 
 
