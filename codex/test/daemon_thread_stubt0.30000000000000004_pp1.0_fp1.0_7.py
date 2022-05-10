import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdin.readline()

def main():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()
