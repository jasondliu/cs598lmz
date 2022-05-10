import sys, threading

def run():
    print "Started"
    time.sleep(1)
    print "Finished"

def run2():
    print "Started"
    time.sleep(3)
    print "Finished"

def run3():
    print "Started"
    time.sleep(5)
    print "Finished"

if __name__ == "__main__":
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=run2)
    t3 = threading.Thread(target=run3)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
