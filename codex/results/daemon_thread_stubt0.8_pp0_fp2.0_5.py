import sys, threading

def run():
    print("Hello from a thread!")

class SimpleThread(threading.Thread):
    def __init__(self, name=None):
        super(SimpleThread, self).__init__()
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name)

# Create two threads as follows
t = SimpleThread(name='Chad')
t2 = SimpleThread(name='Tiffany')
t.start()
t2.start()
