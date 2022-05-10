import sys, threading

def run():
    global thread
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while True:
        if thread.is_alive():
            thread.join(1)
</code>

