import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdin.readline()

def main():
    sys.stdout.write("\n")
    sys.stdout.flush()
    thread = threading.Thread(target=run)
    thread.start()
    while True:
        pass

if __name__ == "__main__":
    main()
