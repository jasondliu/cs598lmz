import threading
# Test threading daemon
def test_threading_daemon():
    print(threading.current_thread().name)
    t = threading.Thread(name='test_threading_daemon_sub', target=test_threading_daemon, daemon=True)
    t.start()
    pass

# Use threading
def test_threading():
    t = threading.Thread(name='test_threading_sub', target=test_threading_sub, args=('test_threading_sub_args0_1', 'test_threading_sub_args0_2'))
    t.setDaemon(True)
    t.start()
    t.join()
    print('main_thread')
    pass

# Use thread class and daemon
def test_threading_sub(param01, param02):
    print(param01, param02)
    pass

if __name__ == '__main__':
    # test_threading()
    test_threading_daemon()
    pass
