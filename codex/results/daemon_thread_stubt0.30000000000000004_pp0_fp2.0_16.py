import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print(line.strip())

t = threading.Thread(target=run)
t.start()

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    print(line.strip())
