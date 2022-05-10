import sys, threading

def run():
    while True:
        print("Hello")
        time.sleep(1)

thread = threading.Thread(target=run)
thread.start()

while True:
    print("World")
    time.sleep(1)
</code>
I want to run this script in the background, so I run it with <code>nohup</code>:
<code>nohup python3 script.py &amp;
</code>
However, when I run this, the script doesn't print anything. I can see that it is running in the background with <code>ps</code>, but it doesn't print anything.
How can I run this script in the background?


A:

The problem is that <code>nohup</code> redirects stdout to a file called <code>nohup.out</code>. You can see this by running <code>nohup python3 script.py</code> and then <code>cat nohup.out</code>.
To fix this, you can redirect stdout to <code>/dev/null</code> with <code>nohup python
