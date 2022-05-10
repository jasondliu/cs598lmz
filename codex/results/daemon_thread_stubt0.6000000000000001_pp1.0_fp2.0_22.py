import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    input = sys.stdin.readline()
    if input == "exit\n":
        sys.exit()
    else:
        sys.stdout.write("Command not recognized.\n")
        run()

threading.Thread(target = run).start()

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    input = sys.stdin.readline()
    if input == "exit\n":
        sys.exit()
    else:
        sys.stdout.write("Command not recognized.\n")
        run()

threading.Thread(target = run).start()

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    input = sys.stdin.readline()
    if input == "exit\n":
        sys.exit()
    else:
        sys.stdout.write("Command not recognized.\n")
        run()

