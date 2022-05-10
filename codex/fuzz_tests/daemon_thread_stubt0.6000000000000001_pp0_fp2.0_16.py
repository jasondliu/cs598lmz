import sys, threading

def run():
    while True:
        print("Threading")

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Main Thread")
    time.sleep(1)
</code>

