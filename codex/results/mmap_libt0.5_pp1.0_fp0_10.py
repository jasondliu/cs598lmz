import mmap

class MyClass(object):
    def __init__(self):
        self.mf = mmap.mmap(-1, 1024*1024*1024)
        self.mf.seek(0)
    def __del__(self):
        self.mf.close()

def myfunc():
    myobj = MyClass()
    myobj.mf.write('hello')
    print myobj.mf.read(5)
    del myobj

myfunc()
</code>
If I run this code, I get the following output:
<code>hello
Exception AttributeError: "'mmap' object has no attribute 'mf'" in &lt;bound method MyClass.__del__ of &lt;__main__.MyClass object at 0xb7d08bcc&gt;&gt; ignored
</code>
I understand that the attribute <code>mf</code> is not available in the <code>__del__</code> method because it has been garbage collected already. But how should I close the file?


A:

<code>__del__
