import threading
# Test threading daemon
def thread_function(name):
    print("Thread {}: starting".format(name))
    time.sleep(2)
    print("Thread {}: finishing".format(name))

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)

# Thread 0: starting
# Thread 1: starting
# Thread 2: starting
# Thread 0: finishing
# Thread 1: finishing

