import sys, threading

def run():
    print('t1 start')
    print('t1 end')

def main():
    print('main start')
    t1 = threading.Thread(target=run, args=())
    t1.start()
    t1.join()
    print('main end')

if __name__ == '__main__':
    main()
