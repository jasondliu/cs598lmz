import threading
# Test threading daemon mode

def func():
    print 'func, thread is %s'%threading.current_thread()
    return

def test_daemon_thread():
    t = threading.Thread(target=func)
    t.setDaemon(True)
    t.start()
    print 'main, thread is %s'%threading.current_thread()
    return

def test_not_daemon_thread():
    t = threading.Thread(target=func)
    t.start()
    print 'main, thread is %s'%threading.current_thread()
    return

if __name__ == '__main__':
    print 'test_daemon_thread...'
    test_daemon_thread()
    print 'main thread exit'
    print 'test_not_daemon_thread...'
    test_not_daemon_thread()
    print 'main thread exit'
