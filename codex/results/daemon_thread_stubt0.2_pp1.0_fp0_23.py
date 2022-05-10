import sys, threading

def run():
    print("Thread started")
    while True:
        pass

threads = []
for i in range(10):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)

print("Started threads")

while True:
    pass
