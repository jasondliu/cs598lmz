import threading
# Test threading daemon
def test_daemon():
    print("Start test_daemon")
    time.sleep(2)
    print("End test_daemon")

d = threading.Thread(name="daemon", target=test_daemon)
d.setDaemon(True)
d.start()

# Test threading non-daemon
def test_non_daemon():
    print("Start test_non_daemon")
    print("End test_non_daemon")

t = threading.Thread(name="non-daemon", target=test_non_daemon)
t.start()

# Main thread
print("Main thread")

# Main thread will wait for non-daemon thread to finish
t.join()

# Main thread will not wait for daemon thread to finish
print("Main thread end")
