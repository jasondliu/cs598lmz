import sys, threading

def run():
    while True:
        print("thread")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

while True:
    print("main")
    time.sleep(1)
</code>
The output is:
<code>main
thread
main
thread
main
thread
main
thread
main
thread
main
thread
</code>

