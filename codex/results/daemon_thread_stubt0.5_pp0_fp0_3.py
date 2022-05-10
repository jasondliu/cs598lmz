import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        print line.upper()

threading.Thread(target=run).start()
