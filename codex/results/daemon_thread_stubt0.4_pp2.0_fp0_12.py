import sys, threading

def run():
    while True:
        print("Running")
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("Main")
    time.sleep(1)
</code>

