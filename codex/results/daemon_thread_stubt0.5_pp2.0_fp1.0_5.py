import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        line = line.strip()
        print("Line:", line)
        sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
