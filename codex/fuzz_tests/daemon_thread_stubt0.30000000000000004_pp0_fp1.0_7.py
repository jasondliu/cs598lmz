import sys, threading

def run():
    global x
    for i in range(1000000):
        x = x + 1

x = 0
t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)
