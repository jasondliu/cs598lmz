import threading
# Test threading daemon
# When the main thread is over, the daemon threads are over.

def thread_job():
    print("This is another thread, number is %s" % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.setDaemon(True)
    added_thread.start()
    print(threading.activeCount())
    print(threading.enumerate())
    print(threading.current_thread())
    print(threading.current_thread().getName())

if __name__ == '__main__':
    main()
