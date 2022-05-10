import sys, threading

def run():
    cmd = "-r" if len(sys.argv) < 2 else sys.argv[1]

    if cmd == "-r":
        threading.Timer(2, run).start()
        call(["make"])

    if cmd == "-c":
        call(["make", "clean"])

run()
