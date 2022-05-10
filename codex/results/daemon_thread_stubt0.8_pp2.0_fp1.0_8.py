import sys, threading

def run():
    for i in range(0, 11):
        print(i)
        time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
    inp = input()
    if inp == "quit":
        sys.exit()
</code>
I've tried it with while True: inp = input() and also with raw_input().
On the console it will print every second a number but when I write quit it stays there. Why? I tried a lot of other methods but nothing seems to work.
My question is not how to quit the thread, just what is wrong with the program-flow.


A:

You should use <code>join</code> to wait for a daemon thread to exit:
<code>t.join()
</code>
From the docs:
<blockquote>
<p>join([timeout])</p>
<p>Wait until the thread terminates. This blocks the calling thread until the thread whose join() method is called terminates – either normally or through an unhandled exception or until the optional
