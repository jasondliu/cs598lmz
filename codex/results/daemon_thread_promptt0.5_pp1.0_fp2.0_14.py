import threading
# Test threading daemon
class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        global y
        lock.acquire()
        for i in range(5):
            y += 1
            print(self.name + str(y))
        lock.release()

# Test threading with return value
def thread_with_return(arg1, arg2):
    print(arg1 + arg2)
    return arg1 + arg2

# Test threading pool
def thread_pool():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

def long_time_task(i):
    print('Run task %s (%s)...
