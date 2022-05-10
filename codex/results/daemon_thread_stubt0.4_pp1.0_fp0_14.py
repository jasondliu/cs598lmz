import sys, threading

def run():
    while True:
        print "."
        time.sleep(1)

def main(argv):
    print "Started"
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

    print "Waiting for input"
    raw_input()

if __name__ == "__main__":
    main(sys.argv)
</code>

