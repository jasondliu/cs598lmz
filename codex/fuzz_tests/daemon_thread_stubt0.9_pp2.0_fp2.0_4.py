import sys, threading

def run():
    global count
    while True:
        count += 1

thread = threading.Thread(target=run)
thread.start()
while 1:
    print("Count =", count)
    sys.stdout.flush()
