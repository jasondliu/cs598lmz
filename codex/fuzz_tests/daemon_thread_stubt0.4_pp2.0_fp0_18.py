import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print("Goodbye")
    time.sleep(1)
</code>

