import sys, threading

def run():
    while True:
        print(threading.current_thread().getName())
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    t.join()

if __name__ == '__main__':
    main()
