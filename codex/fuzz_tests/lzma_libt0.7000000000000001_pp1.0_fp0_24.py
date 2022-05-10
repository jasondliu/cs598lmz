import lzma
lzma.open()
</code>
however, I'm getting this error:
<code>Traceback (most recent call last):
  File "/home/kyle/Desktop/test.py", line 3, in &lt;module&gt;
    lzma.open()
TypeError: open() missing 1 required positional argument: 'filename'
</code>
I'm using python 3.6.4 running on a Linux. 
I have tried looking for a solution online, but nothing seems to have worked. 


A:

The error is self explanatory, you are missing a required positional argument named "filename". 
You need to provide a file name.
Try calling like this:
<code>lzma.open('filename.xz')
</code>

