import threading
# Test threading daemon
import time

def test_thread(delay):
    print("Thread running")
    time.sleep(delay)
    print("Thread done")

# Create thread
thread = threading.Thread(target=test_thread, args=(5,))

# Set as daemon
thread.daemon = True

# Start thread
thread.start()

# Wait for thread to finish
thread.join()

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")
 
# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("Thread finished?")

# Code continues to run here
print("
