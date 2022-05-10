import sys, threading

def run():
    t = threading.currentThread()
    print t.getName()
    print t.isAlive()
    print t.isDaemon()
    print t.getName()
    # print t.isDaemon()
    # t.setName(t.getName() + '_renamed')
    # print t.getName()
    # print t.isDaemon()
    # t.setDaemon(True)
    # print t.isDaemon()

def main():
    print threading.currentThread().getName(), 'start'
    t = threading.Thread(target=run, name='MyThread')
    print t.getName()
    print t.isAlive()
    print t.isDaemon()
    print t.getName()
    # print t.isDaemon()
    # t.setName(t.getName() + '_renamed')
    # print t.getName()
    # print t.isDaemon()
    # t.setDaemon(True)
    # print t.isDaemon()
   
