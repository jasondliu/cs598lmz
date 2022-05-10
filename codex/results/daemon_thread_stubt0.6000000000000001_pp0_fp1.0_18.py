import sys, threading

def run():
    print("hello")
    sys.exit()

t = threading.Thread(target = run)
t.start()
</code>

