from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
python 2.7.6
<code>Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt; from bz2 import BZ2Decompressor
&gt;&gt;&gt; BZ2Decompressor()
&lt;bz2.BZ2Decompressor object at 0x7f2ad23ff170&gt;
</code>
I'm using <code>Python 2.7.6</code> on both linux and Windows. On Linux I had to install <code>bzip2-devel</code>, which I did.
On <code>Windows 8.1</code> I had no such luck. I've looked at the <code>Python</code> distribution and found that <code>bz2.c</code> is indeed there. I have no idea what's going on.
I'm running on <code>VMWare</code>
