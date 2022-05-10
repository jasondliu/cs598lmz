import threading
# Test threading daemon with time.sleep(10)

# This function creates a new thread
def thread_function(name):
    print("Thread {} starting".format(name))
    time.sleep(10) # Wait 10 seconds
    print("Thread {} is done".format(name))

# Create a new thread
thread = threading.Thread(target=thread_function, args=(1,))

# Make the thread a daemon
thread.daemon = True

# Start the thread
thread.start()

input("Press <Enter> to continue...\n")

# Start the main program.
print("Main Program starting")
time.sleep(5) # Wait 5 seconds

print("Main program is done")
