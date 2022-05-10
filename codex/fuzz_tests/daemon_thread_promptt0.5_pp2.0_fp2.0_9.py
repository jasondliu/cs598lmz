import threading
# Test threading daemonic
def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting:', threading.currentThread().getName())

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting:', threading.currentThread().getName())

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# Test the thread
# def worker():
#     """thread worker function"""
#     print('Worker')
#     return
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()

# Test the threading lock
# balance = 0
# lock = threading.Lock()
#
# def change_it
