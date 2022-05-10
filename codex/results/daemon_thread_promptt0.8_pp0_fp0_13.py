import threading
# Test threading daemon
def thread_loop(interval):
    while True:
        print("Thread {} Time: {}".format(threading.current_thread().name, time.ctime()))
        time.sleep(interval)

def main():
    thread_1 = threading.Thread(target=thread_loop, args=(5,), name="Thread-1")
    thread_1.setDaemon(True)
    thread_2 = threading.Thread(target=thread_loop, args=(5,), name="Thread-2")
    thread_2.setDaemon(True)
    thread_1.start()
    thread_2.start()
    time.sleep(6)
    print('Main thread time: {}'.format(time.ctime()))
    print("Number of Threads: ", threading.active_count())
    print("List of Threads: ", threading.enumerate())

if __name__ == "__main__":
    main()
