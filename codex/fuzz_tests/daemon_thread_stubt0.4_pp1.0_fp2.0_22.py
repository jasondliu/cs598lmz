import sys, threading

def run():
    while True:
        print("running")
        time.sleep(1)

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
    print("started")
    time.sleep(5)
    print("exiting")

if __name__ == "__main__":
    main()
</code>

