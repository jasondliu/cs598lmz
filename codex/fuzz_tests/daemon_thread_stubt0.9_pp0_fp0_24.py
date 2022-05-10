import sys, threading

def run():
    for j in xrange(1,100000000):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    pass

# run the threads
threads = []
for i in range(0, len(sys.argv)-1):
    t = threading.Thread(target=run)
    threads.append(t)
    t.start()
    while threading.activeCount() > 3:
        pass
sys.stdout.flush()

#wait for them to finish
for t in threads:
    t.join()
