import threading
# Test threading daemon mode, created thread will auto terminate when main thread terminate

def do_work():
    while True:
        print 'working...'
        time.sleep(2)


if __name__ == '__main__':
    t = threading.Thread(target=do_work)
    t.setDaemon(True) # handle thread exit
    t.start()
    t.join()
    print 'exit main thread'
