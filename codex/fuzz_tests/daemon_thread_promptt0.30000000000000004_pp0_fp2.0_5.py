import threading
# Test threading daemon

def daemon():
    print("Starting daemon thread")
    time.sleep(2)
    print("Finishing daemon thread")

def non_daemon():
    print("Starting non-daemon thread")
    print("Finishing non-daemon thread")

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join()
t.join()

print("Finished")

# Output:
# Starting daemon thread
# Starting non-daemon thread
# Finishing non-daemon thread
# Finished
# Finishing daemon thread

# The daemon thread d is killed before it can finish.

# The daemon thread is killed when the main thread exits.

# The daemon thread d is killed before it can finish.

# The daemon thread is killed when the main thread exits.

# The daemon thread d is killed before it can finish.

# The daemon thread is killed when
