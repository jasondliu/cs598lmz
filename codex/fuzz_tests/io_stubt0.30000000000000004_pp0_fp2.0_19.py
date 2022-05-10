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
del File
</code>
This is a simplified version of the code I am trying to run. I have a class that inherits from <code>io.RawIOBase</code> and has the <code>readinto</code> method. I am trying to use <code>io.BufferedReader</code> to read from it.
The problem is that when I try to delete the <code>File</code> object, I get the following error:
<code>&gt;&gt;&gt; del File
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
NameError: name 'view' is not defined
</code>
I am not sure why this is happening. I thought that the <code>io.BufferedReader</code> object would have a reference to the <code>File</code> object, but it seems that it has a reference to the <code>buf</code> object instead.
Is there any way to get around this?


A:

<code>buf</code> is a local variable, so
