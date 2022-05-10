import threading
threading.stack_size(256*1024)

class Queue:
    def __init__(self):
        self.queue = collections.deque()
    def enqueue(self,x):
        self.queue.appendleft(x)
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return None
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)

class Node:
    def __init__(self,val):
