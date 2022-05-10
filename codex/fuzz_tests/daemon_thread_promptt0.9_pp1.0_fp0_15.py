import threading
# Test threading daemon and non-daemon

def non_daemon():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')


def daemon():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(4)
    print(threading.current_thread().getName(), 'Exiting')


d = threading.Thread(name='daemon', target=daemon, daemon=True)

t = threading.Thread(name='non_daemon', target=non_daemon)

d.start()
t.start()

# d.join()
print(d.isAlive())
print('d.isAlive() = ', d.isAlive())
print(t.isAlive())
print('t.isAlive() = ', t.isAlive())

# print(d.join()) #没有输出
# d.join()
# t.join()
# print('
