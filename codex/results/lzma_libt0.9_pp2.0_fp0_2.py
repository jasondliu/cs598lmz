import lzma
lzma.LZMAError
</code>
resulting in
<code>---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
&lt;ipython-input-8-1b84fc5d539f&gt; in &lt;module&gt;
----&gt; 1 import lzma
      2 lzma.LZMAError

NameError: name 'lzma' is not defined
</code>
On my other computer, running Fedora 27, the two commands execute fine.
I also tried installing <code>pyliblzma</code>, <code>lzma-devel</code> and <code>python3-lzma</code>.
Anyone knows a solution to this?

Python 3.6.5
PIP 10.0.1



A:

The error you're getting is from attempting to import a module that doesn't exist. That is to say, you can't <code>import lzma</code> because you don't have a module named <code>lzma</code>; you have a package named <code>lzm
