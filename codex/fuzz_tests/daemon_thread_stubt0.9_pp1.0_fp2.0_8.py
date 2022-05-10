import sys, threading

def run():
    while True:
        line = sys.stdin.readline().strip()
        if line == "exit":
            return

        print line
        sys.stdout.flush()

if __name__ == "__main__":
    run()
