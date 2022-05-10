import threading
# Test threading daemon

StopThread = False

def myThread( name, event ):
    while True:
        event.wait()
        if StopThread:
            print( "%s interrupted" % name )
            break
        print( "%s running" % name )

    print( "%s threads done" % name)

if __name__ == "__main__":

    event = threading.Event()

    t1 = threading.Thread( target=myThread, args=( "Thread #1", event ) )
    t2 = threading.Thread( target=myThread, args=( "Thread #2", event ) )
    t3 = threading.Thread( target=myThread, args=( "Thread #3", event ) )

    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)

    t1.start()
    t2.start()
    t3.start()

    for i in range(0,4):
        print "Event set -> launch threads"
        event.set()
        time.sleep(1)

