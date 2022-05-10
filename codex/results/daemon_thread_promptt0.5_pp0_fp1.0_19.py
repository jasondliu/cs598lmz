import threading
# Test threading daemon
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

try:
    threading.Thread(target=print_time, args=("Thread-1", 2)).start()
    threading.Thread(target=print_time, args=("Thread-2", 4)).start()
except:
    print("Error: unable to start thread")
