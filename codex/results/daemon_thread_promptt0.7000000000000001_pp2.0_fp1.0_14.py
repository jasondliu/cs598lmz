import threading
# Test threading daemon
# When script finished and exit, daemon thread will interrupt and quit
def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    # Main thread
    added_thread = threading.Thread(target=thread_job)
    added_thread.setDaemon(True)
    added_thread.start()
    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())
    print(added_thread)

if __name__ == '__main__':
    main()

# Multi-threading
import time, threading

# Define a function for the thread
def print_time( threadName, delay ):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print('%s: %s' % (threadName, time.ctime(time.time())))

# Create two threads as follows
try:
    threading.Thread(target=print_time, args=('Thread
