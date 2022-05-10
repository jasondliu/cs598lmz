import sys, threading

def run():
    while True:
        pass

threads = []
for i in range(100):
    t = threading.Thread(target = run)
    t.start()
    threads.append(t)

while True:
    pass
