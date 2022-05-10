import sys, threading

def run():
    while True:
        num = 0
        for i in range(100000):
            num += 1
        print('hello world')
        time.sleep(1)

def run2():
    while True:
        num = 0
        for i in range(100000):
            num += 1
        print('hello world2')
        time.sleep(1)

def main():
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run2)
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()
