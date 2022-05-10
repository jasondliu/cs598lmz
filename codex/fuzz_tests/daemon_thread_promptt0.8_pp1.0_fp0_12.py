import threading
# Test threading daemon

def worker(n):
    while True:
        print('Worker: %s' % n)
        time.sleep(1)

def my_service():
    while True:
        print('my_service')
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=my_service)
    t.setDaemon(True)
    t.start()

    for n in range(1, 6):
        t = threading.Thread(target=worker, args=(n,))
        t.setDaemon(True)
        t.start()

    print('main threading')
    time.sleep(10)
    print('main threading is done')
