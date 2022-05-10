import sys, threading

def run():
    print("Thread started")
    while True:
        print("Thread running")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("Main running")
    time.sleep(1)
</code>
I would expect the output to be:
<code>Thread started
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running
Thread running
Main running

