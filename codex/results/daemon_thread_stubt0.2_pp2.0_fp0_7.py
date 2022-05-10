import sys, threading

def run():
    while True:
        print("Hello from thread")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Hello from main")
    time.sleep(1)
</code>

