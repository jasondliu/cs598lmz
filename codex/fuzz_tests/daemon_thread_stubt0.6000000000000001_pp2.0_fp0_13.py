import sys, threading

def run():
    global stop
    while not stop:
        print("hello")

def main():
    global stop
    stop = False
    thread = threading.Thread(target=run)
    thread.start()

    print("Press any key to stop...")
    sys.stdin.read(1)

    stop = True
    thread.join()
    print("Done")

if __name__ == "__main__":
    main()
</code>

