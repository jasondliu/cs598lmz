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
view
</code>
which gives
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    view
UnboundLocalError: local variable 'view' referenced before assignment
</code>
Is there a way to make <code>view</code> available outside of the <code>f.read(1)</code> call?
(I am using Python 3.4.2)


A:

You are creating a new local variable <code>view</code> by assigning to it in the <code>File.readinto()</code> method, thus shadowing the global <code>view</code>.
Change the assignment to <code>global view; view = buf</code> to assign to the global variable, or remove the <code>global view</code> declaration from the global namespace and just use the <code>view = buf</code> assignment in <code>File.readinto()</code>.
The <code>global</code> statement is only needed when you want to assign to a global variable; use of a global variable only requires that you don
