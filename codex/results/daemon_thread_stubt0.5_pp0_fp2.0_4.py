import sys, threading

def run():
    sys.stdout.write("\n")
    sys.stdout.flush()
    time.sleep(0.1)

t = threading.Thread(target=run)
t.start()

for i in range(5):
    sys.stdout.write("\r%d" % i)
    sys.stdout.flush()
    time.sleep(0.5)

sys.stdout.write("\n")
</code>

