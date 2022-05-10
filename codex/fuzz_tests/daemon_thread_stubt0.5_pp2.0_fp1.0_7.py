import sys, threading

def run():
    global c
    while True:
        c += 1

c = 0
threads = []
for i in range(1000):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(c)
