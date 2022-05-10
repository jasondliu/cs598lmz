import threading
# Test threading daemon
def loop():
    x = 0
    while True:
        print(x)
        x = x ^ 1
        time.sleep(1)
for i in range(2):
    t = threading.Thread(target=loop)
    t.start()

# Test threading lock
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
print(balance)

# Test threading local
local_school = threading.local()
def process_student():
    std = local_school.student

