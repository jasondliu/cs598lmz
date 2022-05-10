import threading
# Test threading daemon mode
def looper():
    threadnum = threading.current_thread()
    print(threadnum)
    while True:
        x = 1+1
    
threading.Thread(target=looper).start()

# Update a list over time
import threading
import time
import random

def printer():
    while True:
        print('Hello')
        time.sleep(random.random())
            
my_thread = threading.Thread(target=printer)

# Start the thread
my_thread.start()


# Use instance variables
import threading

# MyThread class inherits from Thread
class MyThread(threading.Thread):
    def __init__(self, letter):
        super().__init__()
        self.letter = letter
    
        
    def run(self):
        print(self.letter)
        
threading.Thread(target=MyThread, args=('A',)).start()

# Queue items in order
import threading
import time
import random


def printer(results):
	while True:
		#
