import sys, threading

def run():
    print(sys.version)

    for i in range(10):
        print('Thread 1:', i)
        time.sleep(0.1)

def run2():
    print(sys.version)

    for i in range(10):
        print('Thread 2:', i)
        time.sleep(0.1)

def main():
    print(sys.version)

    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run2)

    t1.start()
    t2.start()

    for i in range(10):
        print('Main:', i)
        time.sleep(0.1)

if __name__ == '__main__':
    main()
