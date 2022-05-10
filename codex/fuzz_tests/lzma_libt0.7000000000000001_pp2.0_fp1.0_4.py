import lzma
lzma.open
</code>
<blockquote>
<p>ModuleNotFoundError: No module named 'lzma'</p>
</blockquote>
According to my knowledge, lzma module is built-in on Python 3.3 or later.
I am using Python 3.7.0.
How can I import lzma module?


A:

You'll need to install the module using pip:
<code>pip install pylzma
</code>

