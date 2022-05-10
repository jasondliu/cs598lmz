import threading
# Test threading daemon
def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        print(t.getName())
    t.join()

# Test the threading lock
def f():
    print('thread function')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=f)
        t.setDaemon(True)
        t.start()
    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        print(t.getName())
    t.join()

# Test the threading lock
# lock = threading.Lock
