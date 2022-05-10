import threading
# Test threading daemon
def t1():
    print('t1')
    time.sleep(5)
    print('t1')
    time.sleep(5)
    print('t1')
    time.sleep(5)

def t2():
    print('t2')
    time.sleep(5)
    print('t2')
    time.sleep(5)
    print('t2')
    time.sleep(5)

def t3():
    print('t3')
    time.sleep(5)
    print('t3')
    time.sleep(5)
    print('t3')
    time.sleep(5)

t1 = threading.Thread(target=t1)
t2 = threading.Thread(target=t2)
t3 = threading.Thread(target=t3)
t1.start()
t2.start()
t3.start()
