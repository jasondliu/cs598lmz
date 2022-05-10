import threading
# Test threading daemon mode
def worker():
    print('Worker')
    return

if __name__ == '__main__':
    t = threading.Thread(target=worker, args=())
    t.setDaemon(True)
    t.start()
    t.join()

# Test threading lock
count = 0
def adder():
    global count
    count +=1
    time.sleep(0.5)
    count +=1

def thread_function(name):
    for i in range(2):
        adder()
    print('count =', count)

for i in range(10):
    t = threading.Thread(target=thread_function, args=(i,))
    t.start()

# This is to demostrate the issue with count. As multiple threads access the same resource, it may cause data inconsistency.
# Here with function adder, the result is not what we expected, as the result is not integer all the time.
# We can use threading lock to prevent this issue.
import threading
count = 0
lock = threading.Lock()

