import sys, threading

def run():
    while True:
        x = input("&gt;&gt; ")

threads = []
t = threading.Thread(target=run)
threads.append(t)
t.start()
</code>
and I want to call it in the main.py program so that it runs parallel to the other code


A:

You need your <code>run</code> function to be defined in the same module as <code>main.py</code>. Then, from <code>main.py</code> you can say:
<code>import mymodule

# Start your thread
t1 = threading.Thread(target=mymodule.run)
t1.start()

# Do other stuff, maybe.

</code>

