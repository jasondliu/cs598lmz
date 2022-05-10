import ctypes
ctypes.CDLL('./libfoo.so')
</code>
it works. But I don't understand why <code>import foo</code> does not work.


A:

You need to make sure that you have the <code>__init__.py</code> file in the same folder as the <code>module.so</code> file. This is what tells Python that the folder is a package.

