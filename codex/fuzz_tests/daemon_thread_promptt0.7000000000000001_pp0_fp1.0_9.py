import threading
# Test threading daemon
def testDaemon(num):
    print("Thread:%s started" %num)
    time.sleep(2)
    print("Thread:%s ended" %num)
    #print("Thread:%s ended" % threading.current_thread().getName())

def main():
    # Create a thread
    for i in range(2):
        t = threading.Thread(target=testDaemon,args=(i,),daemon=True)
        #t.setDaemon(True) # Set thread daemon
        t.start()
    #print("All thread started")
    #time.sleep(5)
    #print("All thread ended")
    print("Main thread ended")

if __name__ == '__main__':
    main()
