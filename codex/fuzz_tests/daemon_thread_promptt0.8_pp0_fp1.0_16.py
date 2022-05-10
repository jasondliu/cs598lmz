import threading
# Test threading daemonic mode
#t = threading.Thread(target=hello, args=('a',))
#t.daemon = True
#t.start()
#t.join()

#t = threading.Thread(target=hello, args=('b',))
#t.daemon = False
#t.start()
#t.join()

#print 'main done'

# Test with lock

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print balance

# Test
