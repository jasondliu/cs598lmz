import threading
threading.stack_size(2**27)
import sys

sys.setrecursionlimit(10**7)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeHeight:
    def __init__(self):
        self.n = 0
        self.parent = []
    
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        depth = [0] * self.n
        for i in range(self.n):
            if depth[i] != 0:
                continue
            j = i
            while j != -1:
                if depth[j] != 0:
                    break
                depth[j] = depth[self.parent[j]] + 1
                j = self.parent[j]
        return max(depth)

def main():
    tree = TreeHeight()
    tree.read()

