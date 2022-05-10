import sys, threading

def run():
    sys.stdout.flush()
    sys.stderr.flush()
    for i in range(100):
        print(i)
    sys.stdout.flush()
    sys.stderr.flush()

t = threading.Thread(target=run)
t.start()

print("Running")
sys.stdout.flush()
sys.stderr.flush()
t.join()
print("Done")
