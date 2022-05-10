import threading
# Test threading daemon

def run():
    while True:
        print("Hello")
        time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

t.join(3)
print("end")

# Test threading lock

lock = threading.Lock()

def run2(n):
    lock.acquire()
    global num
    num += n
    lock.release()

num = 0
t1 = threading.Thread(target=run2, args=(1,))
t2 = threading.Thread(target=run2, args=(2,))
t1.start()
t2.start()
t1.join()
t2.join()
print(num)

# Test threading RLock

lock = threading.RLock()

def run3(n):
    lock.acquire()
    lock.acquire()
    global num
    num += n
    lock.release()
    lock.release()

num = 0
t1 = threading.Thread
