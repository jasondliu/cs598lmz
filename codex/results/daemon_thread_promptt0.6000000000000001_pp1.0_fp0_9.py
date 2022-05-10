import threading
# Test threading daemon
# https://stackoverflow.com/questions/19078170/python-threading-daemon-vs-non-daemon-and-joining
# https://stackoverflow.com/questions/38467374/how-to-retrieve-a-value-from-a-running-thread-in-python
# Test threading.Event()
# https://www.tutorialspoint.com/python/python_multithreading.htm

# Test to show that threading.Event() works
def thread_test():
    e = threading.Event()
    def worker():
        print("worker thread is waiting for the event")
        e.wait()
        print("worker thread receives the event and is exiting")
    def main():
        print("main thread is creating the event")
        t = threading.Thread(target=worker)
        t.start()
        print("main thread is waiting for the event")
        e.wait()
        print("main thread receives the event")
        print("main thread is setting the event")
        e.set()
    main()

#
