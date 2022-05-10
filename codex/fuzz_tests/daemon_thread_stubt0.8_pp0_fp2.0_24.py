import sys, threading

def run():
    print("hello world")
    sys.exit()

timer = threading.Timer(5,run)
timer.start()

while 1:
    pass
</code>

