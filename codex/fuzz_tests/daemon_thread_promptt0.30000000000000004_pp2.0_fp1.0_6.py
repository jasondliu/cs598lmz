import threading
# Test threading daemon
def f():
    print 'thread function'
    return

def main():
    thread = threading.Thread(target=f)
    thread.setDaemon(True)
    thread.start()
    thread.join(1)
    print 'thread ended'
    return

if __name__ == '__main__':
    main()
