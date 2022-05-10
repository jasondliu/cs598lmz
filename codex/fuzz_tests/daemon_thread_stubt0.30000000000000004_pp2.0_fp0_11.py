import sys, threading

def run():
    while True:
        print "Hello"
        time.sleep(1)

if __name__ == '__main__':
    t = threading.Thread(target=run)
    t.start()
    t.join()
</code>
I am running this on a Raspberry Pi with Raspbian.
I have tried to run this as root and as a normal user.
I have tried to run this with <code>sudo python test.py</code> and <code>python test.py</code>.
I have tried to run this with <code>sudo python test.py &amp;</code> and <code>python test.py &amp;</code>.
I have tried to run this with <code>sudo python test.py &amp; disown</code> and <code>python test.py &amp; disown</code>.
I have tried to run this with <code>sudo python test.py &amp; disown &amp;&amp; exit</code> and <code>python test.py &amp; disown &amp;&amp; exit</code>.
I have tried to run this
