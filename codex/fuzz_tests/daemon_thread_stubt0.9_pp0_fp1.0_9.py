import sys, threading

def run():
    for i in range(10000):
        for j in range(10000):
            for k in range(10000):
                pass

sys.setcheckinterval(1)

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)
t3 = threading.Thread(target=run)

t1.start(); t2.start(); t3.start()

t1.join(); t2.join(); t3.join()

# Without a lock, the end of the program gets executed too sluggishly.
