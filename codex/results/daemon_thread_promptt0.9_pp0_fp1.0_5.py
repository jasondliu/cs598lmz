import threading
# Test threading daemon..

#Global variables.
total = 0

class Game(threading.Thread):
    def __init__(self, x):
        self.x = x
        threading.Thread.__init__(self)
        self.daemon = True # So that when the main process ends, this daemon thread ends too.

    def run(self):
        global total
        y = 0
        #print "Current thread Id is:", threading.currentThread().getName()
        while y < 15:
            y += 1
            #time.sleep(0.2)
            #print "Current value is:", y, "Current thread Id is:", threading.currentThread().getName()
            total += 1
        print "total count", total
        
def parent_process(count):
    for i in range(count):
        print "Main process is printing!!", i
        t = Game(i)
        t.start()


if __name__ == '__main__':
    parent_process(10)
    #print "Main process is printing!!", i
    print "Completed
