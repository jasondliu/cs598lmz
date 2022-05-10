import sys, threading

def run():
    while True:
        pass

threads = []
for i in range(100):
    threads.append(threading.Thread(target=run))

for t in threads:
    t.start()

while True:
    pass
