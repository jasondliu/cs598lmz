from bz2 import BZ2Decompressor
BZ2Decompressor
</code>
The <code>bz2</code> module is not a package, it's a module. If you <code>import bz2</code>, you're importing the <code>bz2</code> module, not the <code>bz2</code> package.
If you want to import the <code>BZ2Decompressor</code> class from the <code>bz2</code> module, you have to do <code>from bz2 import BZ2Decompressor</code>.

