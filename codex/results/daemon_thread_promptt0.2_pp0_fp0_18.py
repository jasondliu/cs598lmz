import threading
# Test threading daemon
def test_daemon():
    print("start")
    time.sleep(2)
    print("end")

d = threading.Thread(name="daemon", target=test_daemon)
d.setDaemon(True)

d.start()

time.sleep(1)
print("main thread end")

# Test threading lock
lock = threading.Lock()

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
    print("Hello, %s (in %s
