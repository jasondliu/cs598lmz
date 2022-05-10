import sys, threading

def run():
    while True:
        print "running"
        time.sleep(1)

def main():
    print "starting"
    thread = threading.Thread(target=run)
    thread.start()
    print "running"
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print "exiting"
            sys.exit()

if __name__ == "__main__":
    main()
</code>

