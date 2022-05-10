import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

def non_daemon():
    print('start')
    print('end')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print('d.isAlive()', d.isAlive())
print('t.isAlive()', t.isAlive())

# Test threading
def test_threading():
    print('start')
    time.sleep(2)
    print('end')

t = threading.Thread(name='test_threading', target=test_threading)
t.start()
t.join()
print('t.isAlive()', t.isAlive())

# Test multiprocessing
def test_multiprocessing():

