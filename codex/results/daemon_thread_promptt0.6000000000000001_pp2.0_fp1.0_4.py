import threading
# Test threading daemonic
def print_thread(thread):
    print("Thread name: ", thread.name)
    print("Thread is alive: ", thread.is_alive())
    print("Thread daemon: ", thread.daemon)
    print("\n")

def thread_daemon():
    print("Threading daemonic...")
    print("\n")

    t1 = threading.Thread(target=print_thread, name="Thread1", args=(threading.current_thread(),))
    t1.daemon = True
    t1.start()
    t1.join()

    t2 = threading.Thread(target=print_thread, name="Thread2", args=(threading.current_thread(),))
    t2.daemon = False
    t2.start()
    t2.join()

    print("\n")
    print("Thread1 is alive: ", t1.is_alive())
    print("Thread2 is alive: ", t2.is_alive())
    print("\n")
    print("Thread daemon: ", threading.current_thread().da
