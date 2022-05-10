import sys, threading

def run():
    while True:
        print("thread running")
        time.sleep(1)

threading.Thread(target=run).start()

while True:
    print("main thread")
    time.sleep(1)
</code>
This is the output:
<code>main thread
thread running
main thread
thread running
main thread
thread running
main thread
thread running
</code>
I expected the output to be:
<code>main thread
thread running
thread running
thread running
thread running
main thread
</code>
Why is the output not as expected?


A:

The output is not as expected because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is not synchronized.
The output is not synchronized because the output is
