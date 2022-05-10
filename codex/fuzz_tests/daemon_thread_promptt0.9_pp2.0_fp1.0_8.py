import threading
# Test threading daemon and non-daemon features
# Note: On windows, daemon threads can only exit when there is no jobs left
# In the end, all the threads will exit with programs
# Also, the daemon threads cannot be interrupted

def worker(arg, kw):
    print(threading.current_thread().name, ' Starting')
    cur = threading.current_thread()
    result = 0
    while (result < 9):
        print(threading.current_thread().name, ' count=', result)
        result += 1
        time.sleep(1)
    print(threading.current_thread().name, ' Exiting')

def my_service():
    print(threading.current_thread().name, ' Starting')
    cur = threading.current_thread()
    result = 0
    while (result <= 9):
        print(threading.current_thread().name, ' count=', result)
        result += 1
        time.sleep(1)
    print(threading.current_thread().name, ' Exiting')

t = threading.Thread(name='my_service
