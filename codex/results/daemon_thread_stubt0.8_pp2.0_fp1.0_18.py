import sys, threading

def run():
    while True:
        cmd = sys.stdin.readline()
        print cmd

threading.Thread(target = run).start()
