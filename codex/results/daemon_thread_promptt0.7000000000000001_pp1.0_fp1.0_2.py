import threading
# Test threading daemon
def thread_function(name):
    print("Thread %s: starting" %name)
    time.sleep(2)
    print("Thread %s: finishing" %name)

if __name__ == "__main__":
    print("Main: before creating thread")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    print("Main: before running thread")
    x.start()
    print("Main: wait for the thread to finish")
    x.join()
    print("Main: all done")
