from bz2 import BZ2Decompressor
BZ2Decompressor(
    max_length=None
)
</code>
All of which works fine in python 2.7.9
However, with python 3.4 I get this error:
<code>  File "/anaconda/lib/python3.4/site-packages/bz2.py", line 91, in __init__
    self._dstate = BZ2Decompressor._get_state()
TypeError: CObject() takes no arguments
</code>
I am not sure what is going on here. I have tried to search for this but couldn't find anything useful for my case.
I am using iPython-Notebook (4.0.3) to run the code.


A:

<code>BZ2Decompressor(max_length=None)</code> is a valid syntax in Python 2 but not in Python 3, as the <code>max_length</code> parameter has become keyword-only from Python 3.5 onwards. I haven't tried it, but I assume that you can get around this by using the following syntax:
<code>BZ2Decompressor(max_length=None)</code
