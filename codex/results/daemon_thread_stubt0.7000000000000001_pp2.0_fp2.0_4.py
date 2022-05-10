import sys, threading

def run():
    while True:
        if (time.time() - start_time) > (60 * 2):
            sys.exit()
        else:
            print(time.time() - start_time)

t = threading.Thread(target=run)
t.daemon = True
t.start()

start_time = time.time()
while True:
    pass
