import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdin.readline()

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    while True:
        print "Hello"
        time.sleep(1)

if __name__ == "__main__":
    main()
</code>

