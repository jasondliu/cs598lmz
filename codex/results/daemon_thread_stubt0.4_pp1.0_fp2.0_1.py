import sys, threading

def run():
    while True:
        time.sleep(1)
        print 'thread running'

def main():
    t = threading.Thread(target=run)
    t.start()
    t.join()
    print 'thread done'

if __name__ == '__main__':
    main()
