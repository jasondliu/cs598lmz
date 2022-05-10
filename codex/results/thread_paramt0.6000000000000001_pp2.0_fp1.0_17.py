import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from a thread.\n')).start()

# A thread can also be launched using a class that extends the Thread class.
# If a subclass overrides the __init__() method, it must make sure to invoke
# Thread.__init__() to ensure proper initialization of the thread.
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(f'Hello from a thread named {self.name}')

MyThread('Bob').start()

# To pass arguments to a thread's target function, simply include them
# after the name of the target function in the args argument to Thread().
def worker(num):
    """thread worker function"""
    print(f'Worker: {num}')

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Joining threads
#
