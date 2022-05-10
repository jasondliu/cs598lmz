import sys, threading

def run():
    for x in range(0,10):
        sys.stdout.write(str(x) + '\n')
        sys.stdout.flush()
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

def test_thread_1():
    for x in range(10,20):
        sys.stdout.write(str(x) + '\n')
        sys.stdout.flush()
        time.sleep(1)

def test_thread_2():
    time.sleep(2)
    print('test_thread_2')

if __name__ == '__main__':
    thread.join()
    t1 = threading.Thread(target=test_thread_1)
    t2 = threading.Thread(target=test_thread_2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
