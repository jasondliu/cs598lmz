import threading
# Test threading daemon
def test_daemon():
    print 'start'
    time.sleep(2)
    print 'end'

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

d.start()
time.sleep(1)
print d.isAlive()
time.sleep(3)
print d.isAlive()

# Test threading lock
def job1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print 'job1', A
    lock.release()

def job2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 10
        print 'job2', A
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
