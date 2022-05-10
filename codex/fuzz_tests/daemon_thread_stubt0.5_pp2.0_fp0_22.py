import sys, threading

def run():
    while True:
        print('thread running')
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    print('main thread running')
    time.sleep(1)
</code>

