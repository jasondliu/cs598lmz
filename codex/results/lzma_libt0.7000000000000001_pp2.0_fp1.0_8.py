import lzma
lzma.LZMAError: lzma module is not available
</code>
The error seems to be from the dependencies of the package <code>emacs-anaconda-mode</code>.
I installed <code>pip</code> using the instructions on https://pip.pypa.io/en/stable/installing/ , and Python 3.7.1 is the default version on my system.
I have installed the <code>python36</code> package, but Python 3.6 is still not the default version.
<code>$ python3 -V
Python 3.7.1
</code>
I have tried to install <code>emacs-anaconda-mode</code> with different versions of Python, but the <code>lzma</code> error still appears.
How can I fix this?


A:

The <code>lzma</code> module is not included with Python 3.6, but is included with Python 3.7.
It seems that you can't fix this without upgrading to Python 3.7. 
I upgraded my Python to Python 3.7.1, and
