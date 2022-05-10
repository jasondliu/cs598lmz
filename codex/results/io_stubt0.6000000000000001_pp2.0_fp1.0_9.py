import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
</code>
This code gives me a <code>NameError: global name 'view' is not defined</code>, but I do not understand why. The only way I found to make it work is to declare the <code>view</code> variable before the <code>readinto</code> method.
I'm using Python 3.4.


A:

The <code>global</code> statement is only valid in the scope of the function or method where it appears.
From the <code>global</code> statement documentation:
<blockquote>
<p>The <code>&lt;code&gt;global&lt;/code&gt;</code> statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals.</p>
</blockquote>
This means that in the <code>readinto()</code> method, <code>global view</code> is valid, but in the <code>readable()</code> method, it is not.
You can move the <code>global</code> statement to the top of your class and
