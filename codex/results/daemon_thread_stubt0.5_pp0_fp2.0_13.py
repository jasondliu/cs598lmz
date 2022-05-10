import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        print(line)

t = threading.Thread(target=run)
t.start()

while True:
    time.sleep(1)
    print("hello world")
