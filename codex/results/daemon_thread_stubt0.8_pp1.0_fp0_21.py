import sys, threading

def run():
    for i in range(5):
        print('Thread: {}'.format(i))
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    thread.join()
    print(threading.activeCount())
    print(threading.enumerate())
    print(threading.currentThread())
    print('hello main')

if __name__ == '__main__':
    main()
