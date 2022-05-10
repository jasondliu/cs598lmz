import threading
# Test threading daemon

def function1():
    print('function 1')
    return

def function2():
    print('function 2')
    return

def function3():
    print('function 3')
    return

if __name__ == '__main__':
    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)
    t3 = threading.Thread(target=function3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
