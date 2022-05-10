import threading
# Test threading daemon
# https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool


def main():
    # Create the queue
    q = Queue()
    # Create a thread that will put data into the queue
    t = threading.Thread(target=put_data, args=(q,))
    # Set the thread as a daemon thread
    t.daemon = True
    # Start the thread
    t.start()
    # Run the consumer
    consumer(q)


def put_data(q):
    # Put some data into the queue
    for i in range(10):
        q.put(i)
        print('Putting ' + str(i) + ' into the queue')
        time.sleep(1)


def consumer(q):
    # Run until interrupted
    while True:
        # Get some data out of the queue
        data = q.get()
        print('Got ' + str(data) + ' out of the queue')
        # Sleep for a bit
        time.sleep
