import sys, threading

def run():
    print("Thread started")
    time.sleep(1)
    print("Thread ended")

# Create a thread
thread = threading.Thread(target=run)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread finished?")

# Create a thread that raises an exception
def run():
    raise Exception("Something bad happened")

# Create a thread
thread = threading.Thread(target=run)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread finished?")

# Create a thread that raises an exception
def run():
    time.sleep(3)
    raise Exception("Something bad happened")

# Create a thread
thread = threading.Thread(target=run)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread finished?")

# Create a thread that raises an exception
def run():
    time.sleep(3)
