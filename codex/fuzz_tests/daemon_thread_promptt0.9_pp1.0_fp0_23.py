import threading
# Test threading daemon
def test_daemon(name):
    print('Thread: %s' % threading.current_thread())
    time.sleep(10)


if __name__ == "__main__":
    t = threading.Thread(target=test_daemon, name="daemon1")
    t2 = threading.Thread(target=test_daemon, name="daemon2")
    t.setDaemon(True)
    t2.setDaemon(True)
    t.start()
    t2.start()
    time.sleep(1)
