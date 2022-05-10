import sys, threading

def run():
    print("threading is running")
    sys.exit()

t = threading.Thread(target=run)
t.start()
t.join()

print("threading end")
