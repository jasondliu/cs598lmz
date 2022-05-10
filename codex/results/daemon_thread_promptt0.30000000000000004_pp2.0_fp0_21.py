import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

d.start()
d.join()

print('main thread')

# Test threading lock
lock = threading.Lock()

def test_lock(n):
    lock.acquire()
    global num
    num += 1
    lock.release()

num = 0
t_objs = []
for i in range(50):
    t = threading.Thread(target=test_lock, args=(i,))
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()

print('num:', num)

# Test threading local
local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.
