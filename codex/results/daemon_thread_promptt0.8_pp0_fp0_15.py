import threading
# Test threading daemon true.
# The thread will terminate when the main thread terminates.
# If this process is killed by kill -9 from outside, the thread will NOT terminate.
def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T1():
    added_thread = threading.Thread(target=thread_job,name='T1')
    added_thread.setDaemon(True) # set daemon thread, then it will terminate when the main thread terminates.
    added_thread.start()
    print('All done\n')
# Test threading daemon true.
# If this process is killed by kill -9 from outside, the thread will terminate.
def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T1():
    added_thread = threading.Thread(target=thread_job,name='T1')
    added
