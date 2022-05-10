import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(5)
    print('Stop daemon')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    print('Start non-daemon')
    print('Stop non-daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

# Test threading lock
lock = threading.Lock()

def print_num(num):
    lock.acquire()
    print(num)
    lock.release()

threads = []
for i in range(10):
    t = threading.Thread(target=print_num, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# Test threading condition
condition = threading.Condition()

def consumer(cond):
    with
