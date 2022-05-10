import threading
# Test threading daemon
# http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python

def main():
    # Create a thread
    t = threading.Thread(target=worker)
    # Set the thread as a "daemon"
    t.daemon = True
    # Start the thread
    t.start()

    # Wait for the thread to complete
    t.join()

def worker():
    # A while loop that runs forever
    while True:
        print "running"
        time.sleep(1)

if __name__ == "__main__":
    main()
