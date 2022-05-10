import sys, threading

def run():
    sys.stdout.write('[%s] %s\n' % (threading.currentThread().getName(), time.ctime()))
    time.sleep(1)

if __name__ == '__main__':
    t = threading.Timer(5, run)
    t.setName('Timer0')
    t.start()
