import threading
threading.stack_size(2**27)  # to run on 32-bit system!!!


class Node:

    def __init__(self, e, val):
        self.element = e
        self.in_degree = 0
        self.value = val
        self.dependencies = []

    def pretty(self):
        s = str(self.element) + ": indegree: " + str(self.in_degree) + "\n"
        for dep in self.dependencies:
            s += str(dep.element) + " "
        print(s)


class PQ:
    def __init__(self):
        self.array = []

    def insert(self, node):
        self.array.append(node)
        if len(self.array) == 1:
            return
        i = len(self.array) - 1
        while self.array[(i-1)/2].value > self.array[i].value:
            self.swap((i-1)/2, i)
            i = (i-1)/2

    def
