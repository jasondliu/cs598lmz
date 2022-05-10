import threading
# Test threading daemon
class MyThread(threading.Thread):
    def run(self):
        print "I am a thread"
        time.sleep(1)
        print "I am a thread"

def main():
    t = MyThread()
    t.setDaemon(True)
    t.start()
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep(0.1)
    print "Main thread is here"
    time.sleep
