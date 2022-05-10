import threading
# Test threading daemon
"""
threads = []
for i in range(20):
    t = threading.Thread(target=thread_function, args=(i,))
    threads.append(t)
    t.start()
for index, thread in enumerate(threads):
    logging.info("Main    : before joining thread %d.", index)
    thread.join()
    logging.info("Main    : thread %d done", index)
"""
# Test threading daemon with queue
# Using a queue to pass messages between the threads.

def thread_function(name, queue):
    logging.info("Thread %s: starting", name)
    while True:
        queue.put("Run")
        logging.info("Thread %s: working", name)
        # Wait random time before next put
        random.randint(1,3)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
