import threading
threading.stack_size(2**27)
import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = list()
        self.parent = None


def createLevelWiseTree(arr):

    root = TreeNode(int(arr[0]))
    q = [root]
    size = len(arr)

    i = 1
    while i < size:

        parent = q.pop(0)

        childCount = int(arr[i])
        i += 1

        for j in range(0, childCount):

            temp = TreeNode(int(arr[i+j]))
            parent.children.append(temp)
            temp.parent = parent

            q.append(temp)

        i += childCount

    return root


def printTreeDetailed(root):

    if root == None:
        return

