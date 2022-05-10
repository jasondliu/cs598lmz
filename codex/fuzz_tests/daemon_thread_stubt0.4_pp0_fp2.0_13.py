import sys, threading

def run():
    while True:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    print("\nEnter your name: ")
    name = sys.stdin.readline().strip()
    print("Hello %s\n" % name)
</code>

