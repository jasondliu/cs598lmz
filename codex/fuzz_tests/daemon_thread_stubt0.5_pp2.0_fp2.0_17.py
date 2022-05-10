import sys, threading

def run():
    print("hello")
    sys.stdout.flush()
    time.sleep(1)

while True:
    t = threading.Thread(target=run)
    t.start()
</code>
This will print out <code>hello</code> once per second, but the output is not continuous. It will print out <code>hello</code> every few seconds. I want to continuously print out <code>hello</code> every second. Is this possible?

