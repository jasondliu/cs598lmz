import sys, threading

def run():
    try :
        sys.stdin.readline()
        sys.exit(0)
    except KeyboardInterrupt:
        print("Bye")
        sys.exit(0)

def main(msg):
    while True:
        sys.stdout.write("\r%s" % msg)
        sys.stdout.flush()
        time.sleep(0.1)
        thread = threading.Thread(target=run)
        thread.start()

if __name__ == "__main__":
    main("Passive mode on")
