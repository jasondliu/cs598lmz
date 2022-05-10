import threading
# Test threading daemon

def func1():
    print 'T1 starting'
    while True:
        pass
    print 'T1 quitting'

def func2():
    print 'T2 starting'
    while True:
        pass
    print 'T2 quitting'

def main():
    t1 = threading.Thread(target=func1, name='T1')
    t2 = threading.Thread(target=func2, name='T2')
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
    print 'main quit'
