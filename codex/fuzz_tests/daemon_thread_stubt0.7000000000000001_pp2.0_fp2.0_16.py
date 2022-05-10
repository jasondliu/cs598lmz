import sys, threading

def run():
    for i in range(10):
        sys.stdout.write(str(i))
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

timer = threading.Timer(5, run)
timer.start()

while True:
    try:
        pass
    except KeyboardInterrupt:
        break
