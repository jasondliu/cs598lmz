import sys, threading

def run():
    while True:
        print(threading.currentThread().getName())
        time.sleep(1)

for i in range(10):
    threading.Thread(target=run).start()
