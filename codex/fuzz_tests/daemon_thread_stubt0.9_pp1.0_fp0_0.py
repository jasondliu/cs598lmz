import sys, threading

def run():
    line = sys.stdin.readline()
    while line:
        print (line)
        line = sys.stdin.readline()
    return

print ("sys.stdin.readline(): ", sys.stdin.readline())

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

raw_input()
