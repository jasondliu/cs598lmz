import threading
# Test threading daemon
def test_threading_daemon():
    print("Start test_threading_daemon")
    def daemon():
        print("Start daemon")
        time.sleep(2)
        print("End daemon")
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    print("End test_threading_daemon")

# Test threading daemon
def test_threading_daemon_2():
    print("Start test_threading_daemon_2")
    def daemon():
        print("Start daemon")
        time.sleep(2)
        print("End daemon")
    d = threading.Thread(name='daemon', target=daemon)
    d.setDaemon(True)
    d.start()
    d.join()
    print("End test_threading_daemon_2")

# Test threading daemon
def test_threading_daemon_3():
    print("Start test_threading_daemon_3")
    def daemon():
       
