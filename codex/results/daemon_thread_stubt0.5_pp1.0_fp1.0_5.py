import sys, threading

def run():
    while True:
        print("Thread running")
        time.sleep(0.2)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    print("Main thread running")
    time.sleep(0.2)
</code>

