import bz2
bz2.test()
</code>
gives the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'test'
</code>
On the site is advice to run "import bz2" before running "bz2.test()", but that just gives:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'test'
</code>


A:

You are importing the built-in <code>bz2</code> module in your first code example, not the third-party module.
If you see the official documentation, they use <code>import bz2file</code>, not <code>bz2</code>.
The solution is to import the correct module:
<code>import bz2file
bz2file.test()
</code>

