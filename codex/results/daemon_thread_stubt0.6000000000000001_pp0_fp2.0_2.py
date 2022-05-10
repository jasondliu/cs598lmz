import sys, threading

def run():
    print("hello world")
    t = threading.Timer(1.0, run)
    t.start()

run()

print("\nPress Enter to Quit")
sys.stdin.readline()
</code>

