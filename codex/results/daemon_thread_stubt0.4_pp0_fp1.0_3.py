import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line:
            line = line.strip()
            if line == 'close':
                sys.exit()
            else:
                print(line)

t = threading.Thread(target=run)
t.start()
