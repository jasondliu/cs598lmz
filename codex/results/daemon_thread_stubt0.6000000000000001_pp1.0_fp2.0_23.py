import sys, threading

def run():
    sys.stdout.write("\r{}".format(sys.argv[1]))
    sys.stdout.flush()
    while True:
        sys.stdout.write("\r{}".format(sys.argv[2]))
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\r{}".format(sys.argv[1]))
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    pass
