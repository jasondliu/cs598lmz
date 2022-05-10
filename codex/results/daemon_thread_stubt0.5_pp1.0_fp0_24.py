import sys, threading

def run():
    sys.stdout.write("started\n")
    sys.stdout.flush()
    while True:
        pass

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
    sys.stdout.write("exiting\n")
    sys.stdout.flush()

if __name__ == "__main__":
    main()
</code>
Output:
<code>$ python test.py
started
exiting
</code>

