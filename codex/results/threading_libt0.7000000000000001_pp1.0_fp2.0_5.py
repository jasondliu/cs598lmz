import threading
threading.current_thread()

def do_this(what):
    whoami(what)

def whoami(what):
    # print("Thread %s says: %s" % (threading.current_thread(), what))
    print("Thread %s says: %s" % (threading.current_thread().getName(), what))

if __name__ == '__main__':
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=("I'm function %s" % n,))
        p.start()

# import threading
# import time
#
# def worker():
#     """thread worker function"""
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(2)
#     print(threading.currentThread().getName(), 'Exiting')
#
# def my_service():
#     """thread worker function"""
#     print(threading.currentThread().getName(), 'Starting')
#     time.sleep(
