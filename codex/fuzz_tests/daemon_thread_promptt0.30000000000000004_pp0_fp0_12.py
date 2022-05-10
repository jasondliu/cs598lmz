import threading
# Test threading daemon

def run():
    print("Thread is running")
    time.sleep(5)
    print("Thread is done")

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

print("Main thread is done")

# If we set the daemon to False, the main thread will wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not wait for the thread to finish

# If we set the daemon to True, the main thread will not
