import sys, threading

def run():
    while True:
        sys.stdout.write("Hello\n")

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    pass
