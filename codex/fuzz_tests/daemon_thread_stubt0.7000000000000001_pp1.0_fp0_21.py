import sys, threading

def run():
    while True:
        x = raw_input()
        if x == 'exit':
            break
        else:
            print x

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()
</code>
The program will start and wait for input, but when I type exit it just hangs and does not stop.
I am on Windows, running Python 2.7.


A:

I don't think you need the thread here at all. You can just do
<code>x = raw_input()
while x != 'exit':
    print x
    x = raw_input()
</code>

