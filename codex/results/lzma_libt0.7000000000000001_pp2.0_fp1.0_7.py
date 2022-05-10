import lzma
lzma.open()
</code>
but it says:
<code>NameError: name 'lzma' is not defined
</code>
I am a python noob, so I don't know how to go about this. I have been looking around, but the solutions are all too complex for me.


A:

Since you are using Python 3.3, you need to import the <code>lzma</code> module explicitly:
<code>import lzma
lzma.open()
</code>
In Python 3.4, the <code>lzma</code> module was added to the standard library, but that is not so in Python 3.3.

