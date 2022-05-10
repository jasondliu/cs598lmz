import sys, threading

def run():
    while True:
        print 'thread:', threading.currentThread().getName()
        time.sleep(1)

def main():
    threading.Timer(5, run).start()
    threading.Timer(10, run).start()
    threading.Timer(15, run).start()
    threading.Timer(20, run).start()
    threading.Timer(25, run).start()
    threading.Timer(30, run).start()
    threading.Timer(35, run).start()
    threading.Timer(40, run).start()
    threading.Timer(45, run).start()
    threading.Timer(50, run).start()
    threading.Timer(55, run).start()
    threading.Timer(60, run).start()
    threading.Timer(65, run).start()
    threading.Timer(70, run).start()
    threading.Timer(75, run).start()
    threading.Timer(80, run).start()
    threading.Timer(85, run).start()

