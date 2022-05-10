import types
types.__name__
</code>
but this could change (even if old versions are arguably not going to change, I'm not sure that's guaranteed).  Keeping everything in a particular namespace and updating it all at once is less prone to breakage.  (Especially if you're bundling some code with other code like a library).

