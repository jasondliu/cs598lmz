import sys, threading

def run():
    global run_event
    while run_event.is_set():
        print('running')
        time.sleep(1)

run_event = threading.Event()
run_event.set()

t = threading.Thread(target=run)
t.start()

