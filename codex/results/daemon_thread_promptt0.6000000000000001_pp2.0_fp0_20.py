import threading
# Test threading daemon
def daemon():
    print('Start threading')
    time.sleep(2)
    print('End threading')

if __name__ == '__main__':
    d = threading.Thread(name='daemon',target=daemon)
    d.setDaemon(True)
    d.start()
    d.join(1)
    print('Main end')

# Test threading non-daemon
def non_daemon():
    print('Start threading')
    time.sleep(2)
    print('End threading')

if __name__ == '__main__':
    d = threading.Thread(name='daemon',target=non_daemon)
    d.setDaemon(False)
    d.start()
    d.join(1)
    print('Main end')

# Test threading daemon and non-daemon
def daemon_1():
    print('Start threading 1')
    time.sleep(2)
    print('End threading 1')

def non_daemon_2():
    print('Start threading
