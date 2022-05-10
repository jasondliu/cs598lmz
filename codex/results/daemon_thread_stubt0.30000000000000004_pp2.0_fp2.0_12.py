import sys, threading

def run():
    while True:
        print("Hello")

thread = threading.Thread(target=run)
thread.start()

print("Press Enter to exit")
sys.stdin.readline()
</code>

