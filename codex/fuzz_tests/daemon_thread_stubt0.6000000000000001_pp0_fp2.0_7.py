import sys, threading

def run():
    while True:
        s = input()
        print(s)
        sys.stdout.flush()

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    while True:
        s = input()
        print(s)
        sys.stdout.flush()

if __name__ == '__main__':
    main()
