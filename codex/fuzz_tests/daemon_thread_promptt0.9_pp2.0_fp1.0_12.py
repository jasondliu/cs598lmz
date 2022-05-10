import threading
# Test threading daemon?
def test_threading():
    def f():
        print 'thread function'
        return
    thr = threading.Thread(target=f, classname='testclass')

    thr.start()
    thr.join()
    print thr.isAlive()

if __name__ == "__main__":
    test_threading()
