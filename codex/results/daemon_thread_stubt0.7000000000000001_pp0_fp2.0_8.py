import sys, threading

def run():
    while True:
        sys.stdout.write(str(random.randint(0, 9)) + '\n')
        sys.stdout.flush()
        time.sleep(1)

t = threading.Thread(target=run, args=())
t.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    sys.exit()
</code>

