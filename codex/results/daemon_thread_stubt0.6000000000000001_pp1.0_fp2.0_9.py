import sys, threading

def run():
    sys.stdout.write("\n"*10)
    sys.stdout.write("*"*10)
    sys.stdout.write("\n")
    sys.stdout.write("Hello world\n")
    sys.stdout.write("*"*10)
    sys.stdout.write("\n")

threading.Thread(target=run).start()
