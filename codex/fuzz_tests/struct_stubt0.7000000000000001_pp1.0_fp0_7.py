from _struct import Struct
s = Struct.__new__(Struct)
s.__init__()
</code>
But that makes no difference.


A:

This error message is due to the way python imports modules. The <code>_struct</code> module is imported by <code>struct</code> and thus it will only be available after the <code>struct</code> module is imported.
In python 3 you can use <code>importlib.import_module</code> to import the module dynamically.
<code>import importlib
s = importlib.import_module('_struct').Struct()
</code>
This will only import the <code>_struct</code> module if it is not already imported.

