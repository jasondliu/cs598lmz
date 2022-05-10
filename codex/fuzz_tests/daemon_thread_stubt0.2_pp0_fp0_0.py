import sys, threading

def run():
    while True:
        print("running")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("main")
    time.sleep(1)
</code>

