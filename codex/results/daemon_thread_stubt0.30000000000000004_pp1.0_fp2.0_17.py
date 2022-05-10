import sys, threading

def run():
    while True:
        time.sleep(1)
        print 'thread'

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        time.sleep(1)
        print 'main'

if __name__ == '__main__':
    main()
