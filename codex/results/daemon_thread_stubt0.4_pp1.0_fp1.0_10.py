import sys, threading

def run():
    while True:
        print(threading.current_thread().name)

def main():
    t = threading.Thread(target=run, name='MyThread')
    t.start()
    t.join()

if __name__ == '__main__':
    main()
