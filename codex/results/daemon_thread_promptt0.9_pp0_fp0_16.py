import threading
# Test threading daemon

def test_daemon():
    t = threading.current_thread()
    print("%s: Hello world!" % t.name, t.isDaemon())
    # t.daemon = True
    print("%s: Hello world!" % t.name, t.isDaemon())

def test_nondaneon():
    t = threading.Thread(target=test_daemon)
    t.daemon = False
    t.start()

def test_daemon_join():
    for x in range(1,10):
        t = threading.Thread(target=test_daemon)
        t.start()
    t.join()

def test_nondaemon_nojoin():
    for x in range(1,10):
        t = threading.Thread(target=test_daemon)
        t.start()
    t.join()
if __name__ == "__main__":
    test_daemon_join()
    #test_nondaemon_nojoin()
