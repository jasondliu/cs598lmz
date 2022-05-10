import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a, 0)
    print(a)

test_select_mutated()
</code>
This yields a segfault.
<code>$ python3 -O segfault.py
Segmentation fault (core dumped)
</code>
This is a simplified version of what I'm doing, but I'm pretty sure the issue lies here.
<code>def _empty_internal_buffer(self, timeout=0):
    r, w, x = select.select([self], [], [], timeout)
    if self in r:
        self.recv(self.in_buffer_size)
</code>
I've also tried using <code>epoll</code> with the same results. Am I doing something wrong here?

Edit:
I was able to reproduce the issue with the following:
<code>import select

class F:
    def __init__(self):
        self.f = open('/dev/null', 'r')
        self.f.close()

    def fileno(self):

