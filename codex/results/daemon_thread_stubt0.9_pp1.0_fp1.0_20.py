import sys, threading

def run():
    for i in range(1, 101):
        time.sleep(0.1)
        sys.stdout.write("\r%d %%" % i)
        sys.stdout.flush()


t = threading.Thread(target=run)
t.start()

while True:
    try:
        t.join(1)
  
