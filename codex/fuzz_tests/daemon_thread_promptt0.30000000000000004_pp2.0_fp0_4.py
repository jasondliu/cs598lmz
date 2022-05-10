import threading
# Test threading daemon
def test_threading_daemon():
    def daemon():
        print('Starting:')
        time.sleep(2)
        print('Exiting:')
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()

# Test threading daemon
def test_threading_daemon_2():
    def daemon():
        print('Starting:')
        time.sleep(2)
        print('Exiting:')
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    print('d.isAlive()', d.isAlive())
    print('d.name', d.name)
    print('d.ident', d.ident)
    print('d.daemon', d.daemon)
    print('d.is_alive()', d.is_alive())
    print('d.getName()', d.getName())
    print('d.
