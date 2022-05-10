import threading
# Test threading daemon

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# Create two threads as follows
try:
    threading.Thread(target=print_time, args=("Thread-1", 2, 5)).start()
    threading.Thread(target=print_time, args=("Thread-2", 4, 5)).start()
except:
    print("Error: unable to start thread")

while 1:
    pass
