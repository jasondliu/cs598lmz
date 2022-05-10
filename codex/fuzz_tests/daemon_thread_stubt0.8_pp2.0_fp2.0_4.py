import sys, threading

def run():
    sys.stdout.write(str(os.getpid())+": Hello, threding!\n")
    sys.exit()

for i in range(10):
    t = threading.Thread(target=run())
    t.start()
