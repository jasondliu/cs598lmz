import sys, threading

def run():
    while True:
        sys.stdout.write("+")
        sys.stdout.flush()
        sys.stdout.write("-")
        sys.stdout.flush()

def main():
    thread = threading.Thread(target=run)
    thread.start()
    sys.stdout.write("*")
    sys.stdout.flush()
    sys.stdout.write("/")
    sys.stdout.flush()
    thread.join()

if __name__ == '__main__':
    main()
