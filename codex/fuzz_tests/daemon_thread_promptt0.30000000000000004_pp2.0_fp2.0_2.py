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

print('done')

# Test threading.local

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread
