import sys, threading

def run():
    sys.stdout.write(sys.argv[1])
    sys.stdout.flush()
    sys.exit(int(sys.argv[2]))

threading.Thread(target=run).start()
