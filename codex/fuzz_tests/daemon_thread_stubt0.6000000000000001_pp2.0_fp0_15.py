import sys, threading

def run():
    time.sleep(1)
    sys.exit()

for i in range(10):
    threading.Thread(target=run).start()
    print(threading.active_count())
