import sys, threading

def run():
    while True:
        print(threading.current_thread().name)
        time.sleep(1)

def main():
    t = threading.Thread(target=run, name='thread-1')
    t.start()
    t.join()

if __name__ == '__main__':
    main()
