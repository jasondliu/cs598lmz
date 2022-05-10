import threading
# Test threading daemon
def thread_function():
    print("Thread %s: starting" % threading.currentThread().getName())
    time.sleep(2)
    print("Thread %s: finishing" % threading.currentThread().getName())

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, name="my_function")
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

# Test threading
# def do_something():
#     print("Sleeping 1 second")
#     time.sleep(1)
#     print("Done sleeping")
#
# if __name__ == "
