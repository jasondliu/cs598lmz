import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from Thread 2\n')).start()

#Threads can also be started as follows
def action(i):
    print(i**32)

class Power:
    def __init__(self, i):
        self.i = i
    def action(self):
        print(self.i**32)

threading.Thread(target=action, args=(2,)).start()
threading.Thread(target=Power(2).action).start()

#Threads communicate using Queue
from queue import Queue
queue = Queue()

def consumer():
    print('Consumer waiting')
    queue.get()
    print('Consumer done')

threading.Thread(target=consumer).start()

print('Producer putting')
queue.put(object())
print('Producer done')

#Threads synchronize using Event
event = threading.Event()

