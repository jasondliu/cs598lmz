import threading
threading.stack_size(67108864)

def func():
    while True:
        print 'I am alive'
        time.sleep(1)

t = threading.Thread(target=func)
t.start()
</code>
and it works. It prints <code>I am alive</code> every second.
Now, if I change the <code>time.sleep(1)</code> to <code>time.sleep(10)</code>, it starts printing <code>I am alive</code> less frequently. It prints it every 10 seconds.
If I change <code>time.sleep(10)</code> to <code>time.sleep(60)</code> it prints <code>I am alive</code> every 60 seconds.
My question is, why is this happening? What is the reason for this?


A:

<code>time.sleep</code> will sleep for at least the time you pass it.  It may sleep a little longer, depending on how other things are running on your machine.
If you want a more accurate way of sleeping, you can use the <code>timeit</code
