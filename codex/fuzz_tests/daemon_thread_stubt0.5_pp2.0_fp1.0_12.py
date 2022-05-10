import sys, threading

def run():
    sys.stdout.write("RUN\n")
    sys.stdout.flush()
    while True:
        s = input()
        print("ECHO:", s)

t = threading.Thread(target=run)
t.start()

print("HELLO")
sys.stdout.flush()

while True:
    s = input()
    print("ECHO:", s)
