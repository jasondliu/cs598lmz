import sys, threading

def run():
    try:
        while True:
            print 'tick'
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

def main():
    try:
        t = threading.Thread(target=run)
        t.daemon = True
        t.start()
        while True:
            print 'tock'
            sys.stdout.flush()
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        sys.exit()

if __name__ == "__main__":
    main()
</code>

