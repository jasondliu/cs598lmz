import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hi\n")).start()
</code>
what is strange about that?
i'm trying to do the same with:
<code>import Image
threading.Thread(target=lambda: Image.open("blah.jpg")).start()
</code>
which causes an exception because <code>Tk.__init__(self, "blah.jpg")</code> doesn't work properly.
is there a workaround for this?


A:

<code>target</code> needs to be a function, not a lambda (which is an anonymous function).
<code>def target():
    return Image.open("blah.jpg")
</code>

