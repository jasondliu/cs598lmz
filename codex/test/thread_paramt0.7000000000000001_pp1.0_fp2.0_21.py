import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread\n')).start()

# Using threads and passing arguments
# This is a way to tell the thread what function it should run, and what arguments to pass to the function
threading.Thread(target=thread_function, args=('Thread 1',)).start()

# Defining a subclass
class PrintThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        print(f'Thread {self.name}')

# Creating a subclass instance
thread = PrintThread('1')
# Starting the thread
thread.start()

# Using a thread pool
import concurrent.futures, time
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(time.sleep, 1)

# Pass an infinite iterator to a thread pool
def infinite_iterator():
    i = 0
    while True:
        yield i
        i += 1

