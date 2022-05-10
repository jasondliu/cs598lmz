import sys, threading

def run():
    while True:
        print("test")
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    threading.Thread(target=run).start()
    while True:
        line = sys.stdin.readline()
        print(line)

if __name__ == "__main__":
    main()
