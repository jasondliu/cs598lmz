import threading
# Test threading daemon thread

def task1():
    print('Task 1 assigned to thread: {}'.format(threading.current_thread().name))
    print('ID of process running task 1: {}'.format(os.getpid()))
    for i in range(1,6):
        print('Task 1: {}'.format(i))
        time.sleep(1)
    print('Task 1 is done')

def task2():
    print('Task 2 assigned to thread: {}'.format(threading.current_thread().name))
    print('ID of process running task 2: {}'.format(os.getpid()))
    print('Task 2 is done')

def main():
    print('ID of process running main program: {}'.format(os.getpid()))
    print('Main thread name: {}'.format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1
