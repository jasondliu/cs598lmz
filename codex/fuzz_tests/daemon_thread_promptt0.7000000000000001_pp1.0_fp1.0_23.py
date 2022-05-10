import threading
# Test threading daemon
def thread_job():
    print('This is an added Thread, number is %s' % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.setDaemon(True)
    added_thread.start()
    print(threading.active_count()) # Count number of threads, including the main thread
    print(threading.enumerate())
    print(threading.current_thread()) # Main thread

if __name__ == '__main__':
    main()
