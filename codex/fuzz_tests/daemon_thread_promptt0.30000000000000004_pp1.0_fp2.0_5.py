import threading
# Test threading daemon

def run():
    while True:
        print('run')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    while True:
        print('main')
        time.sleep(1)

if __name__ == '__main__':
    main()

# Test threading lock

lock = threading.Lock()

def run():
    global lock
    lock.acquire()
    print('run')
    time.sleep(1)
    lock.release()

def main():
    global lock
    lock.acquire()
    t = threading.Thread(target=run)
    t.start()
    print('main')
    lock.release()

if __name__ == '__main__':
    main()

# Test threading condition

cond = threading.Condition()

def run():
    global cond
    cond.acquire()
    cond.wait()
    print('run')
    cond.
