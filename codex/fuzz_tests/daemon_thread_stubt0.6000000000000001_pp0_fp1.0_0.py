import sys, threading

def run():
    print("this is a thread...")
    sys.exit()

thread = threading.Thread(target=run)
thread.start()

while True:
    pass
