import threading
# Test threading daemon
def clearbeam():

    print('thread started')

    stop_event = threading.Event()

    while not stop_event.is_set():
        # Signal pan and tilt here

        stop_event.wait(.01)

    print('thread ending')

s = threading.Thread(target=clearbeam, daemon=True) # setting daemon as true ends thread when main ends

s.start()
