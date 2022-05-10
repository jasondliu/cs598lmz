import threading
# Test threading daemon
def run_thread(n):
    print('thread %s is running...' % threading.current_thread().name)
    time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=run_thread, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# Test threading lock
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地
