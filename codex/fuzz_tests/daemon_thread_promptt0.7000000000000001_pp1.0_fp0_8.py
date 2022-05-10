import threading
# Test threading daemon.
def daemon():
    print('Starting:', threading.currentThread().getName())
    time.sleep(2)
    print('Exiting :', threading.currentThread().getName())
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
def non_daemon():
    print('Starting:', threading.currentThread().getName())
    print('Exiting :', threading.currentThread().getName())
t = threading.Thread(name='non-daemon', target=non_daemon)
d.start()
t.start()
d.join()
t.join()

# Test GIL.
def countdown(n):
    while n > 0:
        n -= 1
import time
import threading
import multiprocessing
COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1
start = time.time()
countdown(COUNT)
end = time.time()
print('Sequential execution in %.3f seconds' % (end - start
