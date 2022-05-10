import threading
# Test threading daemon
def thread_function(name):
    print("Thread: {}: starting".format(name))
    time.sleep(2)
    print("Thread: {}: finishing".format(name))

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # Logging is a threading-safe operation, so logging from a
    # thread doesn’t require any special locking
   
    logging.info("Main    : all done")

# 透過logging提高程式碼的可讀性(減
