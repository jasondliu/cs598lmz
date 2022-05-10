import sys, threading

def run():
    for i in range(10):
        print(i)
        time.sleep(0.1)

thread = threading.Thread(target=run)
thread.start()

sys.exit()
