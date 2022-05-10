import sys, threading

def run():
    global n
    for i in range(1000000):
        n += 1

n = 0
t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)
t1.start()
t2.start()
t1.join()
t2.join()
print(n)
