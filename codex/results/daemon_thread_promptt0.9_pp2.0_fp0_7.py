import threading
# Test threading daemon and exit
def threading_daemon_join():
    def foobar():
        print('hello')
    t = threading.Thread(target=foobar)
    t.daemon = True
    t.start()
    print('Done1')

if __name__ == '__main__':
    threading_daemon_join()
    print('Done2')
