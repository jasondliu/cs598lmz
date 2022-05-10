import threading
# Test threading daemon

#my_thread = threading.Thread()
#my_thread.setDaemon(True)
#my_thread.start()

#print (my_thread.is_alive())

#my_thread.join(2) # wait for the thread to finish before continuing

#print (my_thread.is_alive())


# Test threading with classes
import time

class Thread_test(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        print('init')
    
    def run(self):
        print('running')
        print_time(self.name, self.delay)

def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name, time.ctime(time.time()))

thread_one = Thread_test('one', 1)
thread_two = Thread_test('two', 2
