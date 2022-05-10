import sys, threading

def run():
    while True:
        sys.stdout.write("<You>:")
        try:
            msg = sys.stdin.readline()
        except KeyboardInterrupt:
            print("Error: KeyboardInterrupt")
            break
        if msg == "quit\n":
            break
        else:
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
            print("<You>:" + msg + "\n")

threading.Thread(target=run).start()
