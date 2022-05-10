import threading
# Test threading daemon
#
#
def test_threading_daemon():
    def thread_func():
        print('thread_func')
        time.sleep(10)
        print('thread_func end')

    thread = threading.Thread(target=thread_func)
    thread.setDaemon(True)
    thread.start()
    print('main thread')
    time.sleep(5)
    print('main thread end')


if __name__ == '__main__':
    test_threading_daemon()
