import threading
# Test threading daemon
def test():
    t=threading.currentThread()
    print(t.name)
    print('[%d] Start' % os.getpid())
    time.sleep(2)
    print('[%d] End' % os.getpid())
 
if __name__ == '__main__':
    # Main process
    print('[%d] Main process start' % os.getpid())
    mtd=threading.Thread(target=test,name='Daemon Thread')
    mtd.setDaemon(True)
    mtd.start()
    time.sleep(1)
    print('[%d] Main process end' % os.getpid())

# The daemon thread is stopped forcibly when the main program stops.
