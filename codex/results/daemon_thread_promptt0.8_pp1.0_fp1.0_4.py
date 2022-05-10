import threading
# Test threading daemon
# A simple daemon
def daemon():
    pid = os.getpid()
    print(pid)
    while True:
        time.sleep(2)

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    pid = os.getpid()
    print(pid)
    time.sleep(3)
    print('End non_daemon')

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

class MyThread(threading.Thread):
    def run(self):
        print(os.getpid())
        time.sleep(1)

th = MyThread()
th.setDaemon(True)
th.start()

def daemon_1():
    p_id = os.getpid()
    time.sleep(1)

def non_daemon_1():
    p_id = os.getpid()
    time.sleep(5)

    t_da
