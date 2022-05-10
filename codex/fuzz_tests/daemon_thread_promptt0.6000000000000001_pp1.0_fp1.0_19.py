import threading
# Test threading daemon mode
def thread_job():
    print('This is an added thread, number is %s' % threading.current_thread())
def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.setDaemon(True)
    added_thread.start()
    print(threading.active_count()) # Return how many threads are alive
    print(threading.enumerate()) # Return a list of all threads are alive
    print(threading.current_thread()) # Return current thread
if __name__ == '__main__':
    main()

# Test threading lock
import threading
def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()
def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()
if __name__ == '__main__':

