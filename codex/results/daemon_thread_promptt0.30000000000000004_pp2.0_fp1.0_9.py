import threading
# Test threading daemon
def test_daemon():
    print('start')
    time.sleep(2)
    print('end')

if __name__ == '__main__':
    t = threading.Thread(target=test_daemon, name='LoopThread')
    t.setDaemon(True)
    t.start()
    t.join()
    print('main thread end')
