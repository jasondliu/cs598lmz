import sys, threading

def run():
    while True:
        sys.stdout.write("*")
        sys.stdout.flush()

c = threading.Thread(target=run)
c.daemon = True
c.start()

print("Press Enter to leave...")
raw_input()
