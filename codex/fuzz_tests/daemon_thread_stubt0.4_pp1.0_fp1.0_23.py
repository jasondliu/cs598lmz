import sys, threading

def run():
    for i in range(100):
        print('hello')
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print('main thread')

if __name__ == '__main__':
    main()
