import threading
# Test threading daemon
def test_thread():
    while True:
        print("test thread")
        time.sleep(1)

# Test threading daemon
def test_thread2():
    while True:
        print("test2 thread")
        time.sleep(1)

# Create thread
thread = threading.Thread(target=test_thread)
thread2 = threading.Thread(target=test_thread2)

# Set thread to daemon
thread.daemon = True
thread2.daemon = True

# Start thread
thread.start()
thread2.start()

# Wait for thread to finish
thread.join()
thread2.join()
