import sys, threading
threading.Thread(target=lambda: sys.stdout.write('thread writing\n')).start()
</code>
This first example does as expected, but if I try to put it in a class method like this:
<code>class Test:
    def __init__(self):
        self.thread = threading.Thread(target=lambda: sys.stdout.write('thread writing\n'))
        self.thread.start()

    def sayHi(self):
        sys.stdout.write("Hi\n")
test = Test()
test.sayHi()
</code>
or this:
<code>class Test:
    def __init__(self):
        self.thread = threading.Thread(target=self.write)
        self.thread.start()

    def sayHi(self):
        sys.stdout.write("Hi\n")

    def write(self):
        sys.stdout.write("thread writing\n")
test = Test()
test.sayHi()
</code>
The output is:
<blockquote>
<pre class="lang-none prettyprint-override"><
