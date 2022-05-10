fn = lambda: None
# Test fn.__code__.co_varnames (or inspect.signature)
del fn
</code>
<blockquote>
<p>pdb</p>
</blockquote>
Unfortunately pdb's <code>list</code> command has never worked with lambdas in CPython's standard implementation.  There are several tickets reporting this (e.g. bpo-1467).  But, as stated in bpo-6161, neither IPython nor pudb work either, so it's unlikely to be fixed soon.
After hitting <code>list</code> (it will drop to prompt without error), I wasn't able to find another non-interactive debugger front-end that would work via the Pygments console, and which would list lambdas the same way that pdb does for normal functions:
<code>pysource.py:10:6:
def newfn(): # stuff
</code>
(The Pygments version outputs: <code>&lt;lambda&gt; at /path/to/pysource.py:1</code>
)

while there are several tickets asking for lambda support, afaict no-one
