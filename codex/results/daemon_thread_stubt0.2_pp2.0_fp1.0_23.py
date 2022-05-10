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

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    run_event.clear()
    t.join()
    print('done')
</code>

