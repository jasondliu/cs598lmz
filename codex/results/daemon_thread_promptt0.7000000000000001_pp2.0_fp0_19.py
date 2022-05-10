import threading
# Test threading daemon and non-daemon

def test(i):
    print 'test %d' % i
    while True:
        time.sleep(1)


def main():
    # here we test two threading with/without daemon
    # daemon thread will be terminated when main thread end
    threading_test = threading.Thread(target=test, args=(1,))
    threading_test1 = threading.Thread(target=test, args=(2,))
    threading_test.setDaemon(True)
    threading_test1.setDaemon(False)
    threading_test.start()
    threading_test1.start()
    time.sleep(3)
    print 'main thread end'

main()
