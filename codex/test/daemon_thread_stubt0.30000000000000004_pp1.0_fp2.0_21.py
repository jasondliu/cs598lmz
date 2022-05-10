import sys, threading

def run():
    while True:
        print("Hello from thread %s" % threading.current_thread())
        sys.stdout.flush()

def main():
    for i in range(5):
        t = threading.Thread(target=run)
        t.start()

if __name__ == "__main__":
    main()
