import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

def main():
    t = threading.Thread(target=run, name='mythread')
    t.start()

if __name__ == '__main__':
    main()
