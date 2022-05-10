import sys, threading

def run():
    sys.stdout.write("run\n")
    sys.stdout.flush()
    sys.stderr.write("error\n")
    sys.stderr.flush()

threading.Thread(target=run).start()

sys.stdout.write("stdout\n")
sys.stdout.flush()
sys.stderr.write("stderr\n")
sys.stderr.flush()

print("done")
