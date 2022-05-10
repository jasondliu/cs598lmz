import sys, threading

def run():
    while True:
        sys.stdout.write("1234567890")
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("*" * 100)
    time.sleep(1)
