import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return u"indented string"
</code>
My question is is this a safe/good way to do indentation of strings/string manipulation?  I have a few follow-up questions:

Presumably for this to be a good way to do indentation it needs to be fast (since interpreted languages like Python are not good for raw speed).  Is this a fast way to indent strings?
It looks like <code>tabulate</code> does string interpolation in the loop, so I interpolated <code>suffix</code> and <code>prefix</code> outside of the loop, which are the two things that change across the loop iterations.  Is this correct/necessary?
In string interpolation like this there seems to be some risk of breaking out of the string.  Am I right in thinking this can be stopped by doing <code>r"..."</code> on the strings I'm interpolating to the format string, so that they can't contain backslashes that might be interpreted as escape characters?



A:

Here's a Python translation of your C code. What's interesting is that it churns through 200MB/sec of text on my desktop
