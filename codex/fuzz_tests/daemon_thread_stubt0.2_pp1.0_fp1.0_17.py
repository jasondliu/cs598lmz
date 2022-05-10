import sys, threading

def run():
    print("Thread started")
    time.sleep(1)
    print("Thread finished")

threads = []
for i in range(5):
    t = threading.Thread(target=run)
    threads.append(t)
    t.start()

print("Threads started")

for t in threads:
    t.join()

print("Threads finished")
