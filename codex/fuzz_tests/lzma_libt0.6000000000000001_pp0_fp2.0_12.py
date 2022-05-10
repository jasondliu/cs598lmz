import lzma
lzma.open(file)
</code>
or
<code>xz.open(file)
</code>
Both of them give the following error:
<code>RuntimeError: cannot determine file type
</code>
I'm using Python 3.5.1.
What is wrong?


A:

I have just tested this in Python 3.5 and it works for me. I would suggest you try uninstalling <code>lzma</code> and <code>xz</code> and then reinstalling them.

