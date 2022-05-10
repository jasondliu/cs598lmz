import threading
# Test threading daemon
def test_daemon():
    print("Start test_daemon")
    time.sleep(2)
    print("End test_daemon")

# Test threading non-daemon
def test_non_daemon():
    print("Start test_non_daemon")
    print("End test_non_daemon")

# Create daemon thread
d = threading.Thread(name='daemon', target=test_daemon)
d.setDaemon(True)

# Create non-daemon thread
t = threading.Thread(name='non-daemon', target=test_non_daemon)

# Start daemon thread
d.start()
time.sleep(1)

# Start non-daemon thread
t.start()

# Wait until non-daemon thread terminates
t.join()
