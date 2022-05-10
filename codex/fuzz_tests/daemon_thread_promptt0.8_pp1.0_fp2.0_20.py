import threading
# Test threading daemon
if __name__ == '__main__':
    def worker(num):
        while True:
            time.sleep(1)
            print num
    t = threading.Thread(target=worker, args=(1,))
    t.daemon = True
    t.start()
    t1 = threading.Thread(target=worker, args=(2,))
    t1.daemon = False
    t1.start()
    print 'main thread'
