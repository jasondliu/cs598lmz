import threading
# Test threading daemon

def f():
    while True:
        pass

for i in range(10):
    t = threading.Thread(target=f, daemon=True)
    t.start()
</code>
I've also tried to use other operators like <code>&lt;</code>, but I get the same error.
I am running Python 3.5.1.


A:

<code>daemon</code> is an argument to <code>Thread</code> object, not a property.
<code>class Thread:
    # ...
    def __init__(self, group=None, target=None, args=(), kwargs=None, *, daemon=None):
        # ...
        self.daemon = daemon
</code>

