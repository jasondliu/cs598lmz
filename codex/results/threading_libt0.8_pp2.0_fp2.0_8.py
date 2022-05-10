import threading
threading.Thread(target=time.sleep, args=(10,)).start()
</code>
What I'm trying to do, is to use the <code>sleep</code> function from a new thread. However, when I try this, I get an error:
<code>threading.Thread(target=time.sleep, args=(10,)).start()

TypeError: 'float' object is not callable
</code>
What's causing this error? How do I fix it?


A:

Adding a new thread to sleep for 10 seconds is a messy way of waiting for 10 seconds. It's much better to use the <code>threading.Timer</code> class:
<code>import threading
def do_something():
    print "time's up"
t = threading.Timer(10, do_something)
t.start()
</code>

