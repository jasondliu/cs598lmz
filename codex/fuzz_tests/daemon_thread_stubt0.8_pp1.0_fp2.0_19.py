import sys, threading

def run():
    for i in range(0, 5000):
        print i
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        t = threading.Thread(target=run)
        t.start()
    except:
        print 'Error: unable to start thread'
    while 1:
        pass
