import threading
# Test threading daemon

def test_daemon():
    print('start')
    time.sleep(5)
    print('end')

def test_no_daemon():
    print('start')
    time.sleep(5)
    print('end')

if __name__ == '__main__':
    d = threading.Thread(name='daemon', target=test_daemon)
    d.setDaemon(True)

    t = threading.Thread(name='non-daemon', target=test_no_daemon)

    d.start()
    t.start()

    d.join()
    t.join()
