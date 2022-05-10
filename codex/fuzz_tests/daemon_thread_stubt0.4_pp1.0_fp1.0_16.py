import sys, threading

def run():
    sys.stdout.write("Hello from Python!\n")
    sys.stdout.flush()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(line)
        sys.stdout.flush()

if __name__ == "__main__":
    threading.Thread(target=run).start()
