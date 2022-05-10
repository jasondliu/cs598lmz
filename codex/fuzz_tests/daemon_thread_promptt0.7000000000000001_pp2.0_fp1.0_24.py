import threading
# Test threading daemon process
def worker():
    print('Worker')
    return

t = threading.Thread(target=worker)
t.setDaemon(True)
t.start()

#t.join()

# Test multiprocessing with daemon processes
import multiprocessing

def worker():
    print 'Worker'
    return

jobs = []
for i in range(5):
    p = multiprocessing.Process(target=worker)
    jobs.append(p)
    p.start()    
    p.join()


# Test multiprocessing with daemon processes
import multiprocessing

def worker(num):
    print 'Worker:', num
    return

jobs = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,)) #Notice the comma
    jobs.append(p)
    p.start()
    p.join()
