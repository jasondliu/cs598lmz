import threading
# Test threading daemon
import time
import queue
import random

class ThreadingTest(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            directory = self.queue.get()
            print(directory)
            self.queue.task_done()

def main():
    queue = queue.Queue()
    # Spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadingTest(queue)
        t.setDaemon(True)
        t.start()
    # Populate queue with data
    for directory in ['dir1', 'dir2', 'dir3', 'dir4']:
        queue.put(directory)
    # Wait on the queue until everything has been processed
    queue.join()

if __name__ == '__main__':
    main()
