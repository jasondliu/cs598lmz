import threading
# Test threading daemon
import time
# Test time.sleep
import os
# Test os.getpid

# There seems to be a limit on the number of threads (256 on Windows)
#  that can be created, so we need to create them in batches
# We will create them in batches of BATCH_SIZE threads
BATCH_SIZE = 10
# We will create a total of NUM_BATCHES batches
NUM_BATCHES = 100

# Global variable that will be shared by all threads
global_value = 0
# Lock to protect access to global variable
my_lock = threading.Lock()


# This is the function that will be executed by each thread
def add_to_value(add_value):
    global global_value
    with my_lock:
        global_value += add_value
    return


# Create all threads
threads = []
for i in range(NUM_BATCHES):
    # Create a batch of BATCH_SIZE threads and start them
    for j in range(BATCH_SIZE):
        t = threading.Thread(target=add_to_value,
                             args
