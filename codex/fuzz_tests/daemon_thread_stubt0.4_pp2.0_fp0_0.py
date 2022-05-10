import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stderr.write("\n")
    sys.stderr.flush()
    sys.exit(0)

threading.Timer(3.0, run).start()

# Read from stdin
while True:
    line = sys.stdin.readline()
    if line == "":
        break
    sys.stdout.write(line)
    sys.stdout.flush()
    sys.stderr.write(line)
    sys.stderr.flush()

sys.stdout.write("\n")
sys.stdout.flush()
sys.stderr.write("\n")
sys.stderr.flush()
sys.exit(0)
