import ctypes
ctypes.cast(0, ctypes.py_object).value = 3
</code>
But this solution is just ugly.
I'm looking for an elegant and pythonic solution.
Thanks in advance for your answer.


A:

It is not possible to access the <code>&lt;module '__main__' (built-in)&gt;</code> object after the code is executed.
The way that the main module works doesn't allow it to be accessed like a normal module represented by a <code>&lt;module xyz&gt;</code> object.  What is <code>__main__</code> module in Python?
Specifically the main module is really a special class in the <code>runpy</code> module with methods like <code>run_module</code> and <code>run_path</code>.  If you were to import a .py file, you get an actual <code>module</code> object, if you were to run a .py file from the command line (or equivalent) it will use the default <code>runpy.run_module</code> which uses a special instance of <code>runpy.
