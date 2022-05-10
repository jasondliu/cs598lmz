import threading
# Test threading daemon
def test_daemon():
    print('Start test_daemon')
    time.sleep(10)
    print('End test_daemon')

if __name__ == '__main__':
    print('Start main threading')
    t = threading.Thread(target=test_daemon, args=())
    t.setDaemon(True)
    t.start()
    t.join()
    print('End main threading')
