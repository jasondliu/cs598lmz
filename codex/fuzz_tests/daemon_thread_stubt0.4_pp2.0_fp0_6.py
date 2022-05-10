import sys, threading

def run():
    while True:
        print("running")
        time.sleep(1)

def main(argv):
    t = threading.Thread(target=run)
    t.start()
    while True:
        print("main")
        time.sleep(1)

if __name__ == "__main__":
    main(sys.argv[1:])
</code>

