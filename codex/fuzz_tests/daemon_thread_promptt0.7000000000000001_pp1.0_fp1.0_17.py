import threading
# Test threading daemon and work with Queue

# This function is what the thread runs
def threaded_function(arg,q):
    print('Threaded function starting: ')
    sleep(1)
    print('Threaded function finishing: ')
    q.put(arg)

# Main function
if __name__ == "__main__":
    q = Queue.Queue()  # Queue for threads

    for i in range(10):
        print('Main program starting thread: {0}'.format(i))
        t = threading.Thread(target=threaded_function, args=(i,q))  # Define the thread
        t.setDaemon(True)  # Make the thread a daemon
        t.start()  # Start the thread
        print('Main program waiting on queue: {0}'.format(i))
        q.get()  # Block until queue is populated
        print('Main program got queue: {0}'.format(i))
    print('Main program finishing')
