import sys, threading

def run():
    while True:
        print("Hello from thread", threading.currentThread().getName())
        time.sleep(1)

for i in range(4):
    t = threading.Thread(target=run)
    t.start()

while True:
    print("Hello from main thread", threading.currentThread().getName())
    time.sleep(1)
