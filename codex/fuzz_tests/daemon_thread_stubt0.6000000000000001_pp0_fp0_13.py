import sys, threading

def run():
    while True:
        print('Hello')
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

print('Main thread')
while True:
    time.sleep(1)
</code>

