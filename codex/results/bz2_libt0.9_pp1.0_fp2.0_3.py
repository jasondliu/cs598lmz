import bz2
bz2.BZ2File(loc)  #Error
</code>
Error:
<code>---------------------------------------------------------------------------

IOError                                   Traceback (most recent call last)

&lt;ipython-input-10-2a850f6c194b&gt; in &lt;module&gt;()

----&gt; 1 bz2.BZ2File(loc)

/usr/lib64/python2.7/bz2.pyc in __init__(self, name, mode, compresslevel)

208         try:

209             if name.endswith(".bz2"):

 --&gt; 210                 self.name = name[:-4]

211 

212             if 'r' in mode:



IOError: [Errno 2] No such file or directory: '/filelocation/file.csv.txt'
</code>


A:

The reason you are getting the error is that <code>bz2.BZ2File(loc)</code> fails because the <code>.bz2</code> extension is not present in
