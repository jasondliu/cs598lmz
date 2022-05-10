import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print view
</code>
=========================================================================
I'm new to python, so I'm trying to understand the cpython sourcecode
I think in cpython's interpreter, the source code compiled by py_compile.compile() function is converted to ostream and then written to file "(somefile).pyc" (by use of code_gen.Writer())
My questions are:

Is my understanding above correct?
How can I write a file with pyo/pyc
format? (to produce a buffer)



A:

I used to write my own pyc files in Python 2. I haven't had to in Python 3.
The best documentation for the pyc format that I know of is this PEP.
But there's another way to do what you're trying to do.
When Python imports modules, it puts them into a dictionary <code>sys.modules</code>. If you put one in there, it'll think that that's where your module came from.
As an example, let's say you have a module that you want to import called <code>mymodule</code> that contains a variable <code>x</code>. You would
