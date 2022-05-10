import sys, threading

def run():
    for i in range(5):
        sys.stdout.write('thread1 \n')
        time.sleep(1)

def run2():
    for i in range(5):
        sys.stdout.write('thread2 \n')
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t2 = threading.Thread(target=run2)
    t2.start()
    print("main thread over")
