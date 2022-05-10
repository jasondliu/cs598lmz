import sys, threading

def run():
    while True:
        print("hello")
        time.sleep(1)

t = threading.Thread(target=run)
t.start()

while True:
    print("world")
    time.sleep(1)
</code>
I want to run this script in the background (so I can close the terminal) and I want to be able to kill it if I want to.
I tried <code>nohup python3 script.py &amp;</code> but it doesn't work.
I also tried <code>nohup python3 script.py &gt; /dev/null 2&gt;&amp;1 &amp;</code> but it doesn't work either.
I'm using Ubuntu 18.04.


A:

I think you are looking for the <code>disown</code> command.
<code>nohup python3 script.py &amp;
disown
</code>
This will run the script in the background, and then disown it from the terminal.

