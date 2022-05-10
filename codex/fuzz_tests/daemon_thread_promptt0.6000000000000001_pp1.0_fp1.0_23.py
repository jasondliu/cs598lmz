import threading
# Test threading daemon

def main():
    print(threading.current_thread().getName(), 'Starting')
    bg_th = threading.Thread(target=background_thread, name='Background')
    bg_th.setDaemon(True)
    bg_th.start()
    print(threading.current_thread().getName(), 'Exiting')

def background_thread():
    print(threading.current_thread().getName(), 'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(), 'Exiting')

if __name__ == '__main__':
    main()

# no output from background_thread() in console

# can also set daemonic property to True when creating thread
# daemonic property is inherited by child threads to the parent thread
# threading.main_thread() is never a daemonic thread
# if any non-daemonic thread exits, the program exits immediately

# if a thread is not daemonic and the program exits, the thread continues to run

# program exits when only daemonic threads are left

# thread
