import threading
# Test threading daemon

def test_daemon():
    print('test_daemon')
    print(threading.current_thread().name)
    print(threading.current_thread().isDaemon())
    print(threading.current_thread().ident)

def test_non_daemon():
    print('test_non_daemon')
    print(threading.current_thread().name)
    print(threading.current_thread().isDaemon())
    print(threading.current_thread().ident)

if __name__ == '__main__':
    print('main')
    print(threading.current_thread().name)
    print(threading.current_thread().isDaemon())
    print(threading.current_thread().ident)
    t1 = threading.Thread(target=test_daemon, name='test_daemon', daemon=True)
    t2 = threading.Thread(target=test_non_daemon, name='test_non_daemon')
    t1.start()
    t2.start()
