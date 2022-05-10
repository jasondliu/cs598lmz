import threading
# Test threading daemon mode
def print_time(n,wait_time_secs):
    for x in range(n):
        print 'Time {}'.format(datetime.datetime.now())
        time.sleep(wait_time_secs)

t1 = threading.Thread(target=print_time, args=(5,1))
t1.setDaemon(True)  #true means the main program will not wait for this t1 to finish
t1.start()
print 'Main ended'

# Test lock
lock = threading.Lock()
lock.acquire()
lock.release()

# Test RLock
rlock = threading.RLock()
rlock.acquire()
rlock.release()
rlock.acquire()
rlock.release()

# Test semaphore
def sub_thread(semaphore):
    semaphore.acquire()
    time.sleep(0.5)
    semaphore.release()

def main_thread():
    semaphore = threading.BoundedSemaphore(10) #bound number of threads at the
