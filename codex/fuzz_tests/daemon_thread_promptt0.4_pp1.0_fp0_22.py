import threading
# Test threading daemon
def daemon():
    print('Start')
    time.sleep(2)
    print('End')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
d.start()

# d.join()

# Test threading lock
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
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
print(balance)

# Test threading local
local_school = threading.local()

def process_student():
    std =
