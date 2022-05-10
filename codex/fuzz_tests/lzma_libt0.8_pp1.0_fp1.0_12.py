import lzma
lzma.open
lzma.start_decompressor()
</code>
I have an .xz file I need to extract, so I can use it. I'm been using xz for the command line using <code>xz -d &lt;filename&gt;.xz</code>, but I'd like to do this all within python using python's xz, or gzip libraries. 
I've looked at the python documentation for LZMA, but nothing shows me how to open an .xz file with python. 
Currently, I have a windows 7 machine, with python 3.3.2, and lzma 5.01 installed. I would like to use the binary build of lzma if possible. 


A:

This is more of a comment, but I don't have the rep to comment.
Some options:

Here is an example of extracting xz files (piping the output to stdout)

<blockquote>
<pre><code>&lt;code&gt;import lzma, os
from subprocess import Popen, PIPE
from contextlib import contextmanager

@
