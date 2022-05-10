import threading
# Test threading daemon
def thread_test():
    while True:
        print("Threading test")
        time.sleep(1)

# Create thread
t = threading.Thread(target=thread_test)
# Set thread as daemon
t.setDaemon(True)
# Start thread
t.start()

# Main thread
while True:
    print("Main thread")
    time.sleep(1)

# Main thread will be killed when all non-daemon threads are killed
# In this case, main thread will be killed when t is killed
# t is killed when main thread is killed
# So, main thread will be killed when main thread is killed
# This is an infinite loop
# To stop this, press Ctrl+C
