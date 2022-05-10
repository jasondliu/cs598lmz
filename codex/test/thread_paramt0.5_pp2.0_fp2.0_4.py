import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 1\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Hello from thread 2\n')).start()

# As a function
def hello():
    sys.stdout.write('Hello from thread 1\n')

threading.Thread(target=hello).start()

# As an object
class Hello(threading.Thread):
    def run(self):
        sys.stdout.write('Hello from thread {}\n'.format(self.getName()))

Hello().start()

# As a subclass
class Hello(threading.Thread):
    def run(self):
        for i in range(2):
            sys.stdout.write('Hello from thread {}\n'.format(self.getName()))

Hello().start()
