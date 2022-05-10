import sys, threading

def run():
    print("run")
    sys.exit()

thread = threading.Thread(target=run)
thread.start()

print("main")
