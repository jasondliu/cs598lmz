import threading
# Test threading daemon mode
def test_threading_daemon():
    # Create a thread
    t = threading.Thread(target=lambda: time.sleep(10))
    # Set the thread as daemon thread
    t.setDaemon(True)
    # Start the thread
    t.start()
    # Wait for the thread to finish
    t.join()
    # Print a message
    print('Done')
# Test threading daemon mode
test_threading_daemon()

# Create a thread
t = threading.Thread(target=lambda: time.sleep(10))
# Set the thread as daemon thread
t.setDaemon(True)
# Start the thread
t.start()
# Wait for the thread to finish
t.join()
# Print a message
print('Done')

# Create a thread
t = threading.Thread(target=lambda: time.sleep(10))
# Set the thread as daemon thread
t.setDaemon(True)
# Start the thread
t.start()
# Wait for the thread to finish
t.join()
# Print a message
print('
