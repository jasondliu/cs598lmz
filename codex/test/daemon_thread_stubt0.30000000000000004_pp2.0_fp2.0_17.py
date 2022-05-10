import sys, threading

def run():
    print("run")
    sys.stdout.flush()

t = threading.Thread(target=run)
t.start()

print("main")
sys.stdout.flush()
