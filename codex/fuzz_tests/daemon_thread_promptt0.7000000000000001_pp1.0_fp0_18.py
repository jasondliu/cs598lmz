import threading
# Test threading daemon.

#import logging
#logging.basicConfig(level=logging.DEBUG,
#                    format='(%(threadName)-9s) %(message)s',)

class TimerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.is_running = True

    def run(self):
        print "Starting timer thread"
        while self.is_running:
            print 'Tick'
            time.sleep(1)
            
        print "Thread finished"

    def stop(self):
        self.is_running = False

def main():
    t = TimerThread()
    t.daemon = True
    t.start()
    time.sleep(3)
    t.stop()

if __name__ == '__main__':
    main()
