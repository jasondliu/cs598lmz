import threading
# Test threading daemon
def f(n):
    for i in range(n):
        print 'iteration ', i
        print 'thread alive ', threading.current_thread().is_alive()
        time.sleep(2)
        if i == 3:
            threading.current_thread().is_alive()
            return

# Test normal threading
def ff(n):
    for i in range(n):
        print 'iteration ', i
        time.sleep(2)
        if i == 3:
            return

if __name__ == '__main__':
    t = threading.Thread(target=ff, args=(5,))
    #print 'start'
    t.start()
    #print 'isAlive ', t.isAlive()
    t.join()
    print 'end'
