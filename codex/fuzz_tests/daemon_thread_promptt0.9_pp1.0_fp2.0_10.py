import threading
# Test threading daemon
import time
import psutil
import socket

queue = Queue.Queue()
print('Parent:', os.getpid())
p = psutil.Process(os.getpid())
print('Children:', p.children(recursive=True))

class Worker(object):
    def __init__(self):
        self.index = 0
        self.name = 'thread'+str(self.index)

    def add(self):
        if self.index < 100:
            self.index += 1
            return self.index
        else:
            return self.index

    def put(self):
        try:
            print('Put index: ', self.add())
            queue.put(self.name+' index:'+str(self.add())+' time: '+str(time.time()))
        except Queue.Full:
            print('Error: The queue is full!')

    def get(self):
        try:
            # Get data from queue, block is True
            data = queue.get(False) #block = True
            print('Get data: %
