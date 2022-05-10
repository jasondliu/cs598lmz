import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stderr.write("\n")
    sys.stderr.flush()
    time.sleep(1)
    sys.stdout.write("\r")
    sys.stdout.flush()
    sys.stderr.write("\r")
    sys.stderr.flush()

threading.Thread(target=run).start()

while True:
    sys.stdout.write(".")
    sys.stdout.flush()
    sys.stderr.write(".")
    sys.stderr.flush()
    time.sleep(1)
