import sys, threading

def run():
    while True:
        print 'thread running'
        time.sleep(1)

def main():
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        print 'main thread running'
        time.sleep(1)

if __name__ == '__main__':
    main()
