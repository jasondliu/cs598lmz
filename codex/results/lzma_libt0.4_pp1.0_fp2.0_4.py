import lzma
lzma.LZMAError:
</code>
I am using python 3.7.3 and the latest version of lzma. I have tried using the command <code>pip install backports.lzma</code> and <code>pip install backports.lzma --user</code> and I still get the same error.


A:

I was having the same issue. I was able to resolve it by installing the backports.lzma package.
<code>pip install backports.lzma
</code>

