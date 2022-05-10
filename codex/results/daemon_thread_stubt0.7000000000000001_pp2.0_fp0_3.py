import sys, threading

def run():
    while True:
        # do something
        pass

def main():
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()

    while True:
        # do something
        pass

if __name__ == '__main__':
    main()
</code>
This works fine, but I'm wondering if there's a way to set the daemon flag in a more concise way. E.g. something like this:
<code>t = (threading.Thread(target=run)
          .setDaemon(True)
          .start())
</code>
Doing something like this gives the following error:
<code>Traceback (most recent call last):
  File "sth.py", line 12, in &lt;module&gt;
    .setDaemon(True)
AttributeError: 'NoneType' object has no attribute 'setDaemon'
</code>


A:

You can't do what you want because <code>Thread.start()</code> returns <code>None</code>, so the chain is broken.
