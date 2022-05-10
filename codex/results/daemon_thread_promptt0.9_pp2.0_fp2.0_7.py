import threading
# Test threading daemonic
def test():
    # Do something
    sleep(1)

# Create thread
t = threading.Thread(target=test)
# Set up thread to be a daemon
t.setDaemon(True)
# Start the thread
t.start()
print(t.isDaemon())
# Wait before the main thread exists

# # Test threading join
# def test():
#     # Do something
#     sleep(1)

# # Create thread
# t = threading.Thread(target=test)
# # Start the thread
# t.start()
# # Wait for the thread to finish
# t.join()
