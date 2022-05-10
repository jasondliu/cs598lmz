import sys, threading

def run():
    global count
    while True:
        count += 1
        if count == 1000000:
            break

count = 0

t1 = threading.Thread(target=run)
t1.start()

t2 = threading.Thread(target=run)
t2.start()

t1.join()
t2.join()

print(count)
