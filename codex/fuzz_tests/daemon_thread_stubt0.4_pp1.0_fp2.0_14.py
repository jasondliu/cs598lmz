import sys, threading

def run():
    while True:
        print 'Thread'
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.setDaemon(True)
    t.start()
    print 'Main'
    time.sleep(3)
    print 'Main end'
