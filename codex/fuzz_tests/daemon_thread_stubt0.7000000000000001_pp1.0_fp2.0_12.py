import sys, threading

def run():
    sys.stdout.write("Hello World\n")
    sys.stdout.flush()


threads = []
for i in range(10):
    t = threading.Thread(target=run)
    t.start()
    threads.append(t)
    time.sleep(2)

for t in threads:
    t.join()
