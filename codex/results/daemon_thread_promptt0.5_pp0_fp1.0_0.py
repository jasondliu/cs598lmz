import threading
# Test threading daemon
def test_thread_daemon():
    def daemon():
        print('Start')
        time.sleep(1)
        print('End')

    d = threading.Thread(target=daemon)
    d.setDaemon(True)
    d.start()
    print('Main')

# Test threading non-daemon
def test_thread_non_daemon():
    def daemon():
        print('Start')
        time.sleep(2)
        print('End')

    d = threading.Thread(target=daemon)
    d.setDaemon(False)
    d.start()
    print('Main')

# Test process daemon
def test_process_daemon():
    def daemon():
        print('Start')
        time.sleep(2)
        print('End')

    d = multiprocessing.Process(target=daemon)
    d.daemon = True
    d.start()
    print('Main')

# Test process non-daemon
def test_process_non_daemon():
    def daemon():
        print
