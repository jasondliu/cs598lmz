import threading
# Test threading daemon

import threading, thread
import time

class timer(threading.Thread):
    
    def __init__(self, name, delay, repeat):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay
        self.repeat = repeat
        self.running = False
        
    def run(self):
        print 'Starting ' + self.name
        self.running = True
        while self.running:
            time.sleep(self.delay)
            print self.name, 'D: ', str(self.delay)
            if self.repeat == 0:
                self.running = False
            elif self.repeat > 0:
                self.repeat -= 1
                
    def _stop(self):
        self.running = False
    
    
t1 = timer('t1', 0.5, 5)
t2 = timer('t2', 1.5, 7)

t1.start()
t2.start()
for i in range(5,0,-1):
    print 'D:' , i

