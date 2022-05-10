import threading
# Test threading daemon

def test_daemon():
    print('start')
    time.sleep(2)
    print('exit')

if __name__ == '__main__':
    d = threading.Thread(target=test_daemon)
    d.setDaemon(True)
    d.start()
    d.join(timeout=1)
    print('main thread')

'''
start
main thread
exit
'''
