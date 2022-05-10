from lzma import LZMADecompressor
LZMADecompressor()
</code>


A:

According to the lzma documentation, you have to instantiate the lzma class with a <code>filters</code> parameter.  It doesn't have to be a complicated thing; try <code>filters=[]</code>.
Remember, the <code>__init__</code> method of the class is executed when you call the class as a function (ie. when you call <code>LZMADecompressor()</code>), so whatever parameters you pass to the class will be sent as parameters to <code>__init__</code>.

