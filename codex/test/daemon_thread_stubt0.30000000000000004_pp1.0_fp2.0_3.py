import sys, threading

def run():
    print("run")
    sys.exit(0)

threading.Thread(target=run).start()

print("main")
