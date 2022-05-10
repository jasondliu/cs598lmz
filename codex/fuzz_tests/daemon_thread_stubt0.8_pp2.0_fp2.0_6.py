import sys, threading

def run():
    sys.stdout.write('hello\n')
    sys.stdout.flush()
    exit()

run()
t = threading.Thread(target=run)
t.start()
t.join()
print 'foo'
</code>
This prints:
<code>foo
</code>
It also prints <code>foo</code> in Python 2.7.  However, switching to <code>gevent</code>, we see:
<code>$ python test.py 
hello
foo
</code>
In general, there isn't a good way to avoid this.  Python isn't getting the data until it's too late.  The only way to avoid this is by calling <code>sys.stdout.flush()</code> manually, which is exactly what <code>gevent</code> does for you automatically when you <code>import gevent</code>.

