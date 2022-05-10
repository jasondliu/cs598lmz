import threading
threading.current_thread().name

import threading
lock = threading.Lock()
lock.name

lock.acquire()

lock.release()

class TestThread(threading.Thread):
    #def __init__(self, threadID, name, counter):
    def __init__(self, arg_list):
        threading.Thread.__init__(self)
        self.t1 = arg_list[0]
        self.t2 = arg_list[1]
        return

    def run(self):
        print("Starting " + self.name)
        # Get lock to synchronize threads
        #threadLock.acquire()
        print_time(self.name, self.t1, self.t2)
        # Free lock to release next thread
        #threadLock.release()
        
threadLock = threading.Lock()
threads = []



import threading
lock = threading.Lock()

with lock:
    print('Lock is held')

lock.acquire()
