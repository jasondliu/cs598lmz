import threading
# Test threading daemon
def daemon():
    print('Start daemon')
    time.sleep(0.2)
    print('Exit daemon')
# Test threading non-daemon
def non_daemon():
    print('Start non_daemon')
    print('Exit non_daemon')



if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)

    t = threading.Thread(name='non-daemon', target=non_daemon)

    d.start()
    t.start()
    # d.join()
    # t.join()

    print('Main thread exit!')
