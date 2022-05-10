import sys, threading

def run():
    print("run")
    return

t = threading.Thread(target=run)
t.start()
t.join()

print("end")
