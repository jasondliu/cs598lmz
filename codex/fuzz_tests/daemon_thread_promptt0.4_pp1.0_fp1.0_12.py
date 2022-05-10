import threading
# Test threading daemon
def func():
    print('threading daemon func')
    time.sleep(2)
    print('threading daemon func end')

t = threading.Thread(target=func,daemon=True)
t.start()
print('main thread end')

# Test threading lock
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

balance = 0
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

# Test threading local
local_school = threading.local()
def process_student():
    std = local_school.
