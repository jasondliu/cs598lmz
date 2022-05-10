import sys, threading

def run():
    global event
    while True:
        event.wait()
        print('thread running')
        event.clear()

event = threading.Event()
t = threading.Thread(target=run)
t.start()

while True:
    event.set()
    time.sleep(1)
