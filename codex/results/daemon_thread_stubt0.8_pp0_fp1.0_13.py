import sys, threading

def run():
    raise Exception

threads = []
for i in range(100):
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    threads.append(thread)
