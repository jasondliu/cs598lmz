import bz2
bz2.BZ2File(...)
import lzma
lzma.LZMAFile(...)
</code>
But this will not work on Windows, because lzma is not included in the Python standard library on Windows.
3. Use a subprocess
If you're sure that you have the <code>xz</code> command line tool available, you can just call it as a subprocess:
<code>import subprocess
import io

f = io.TextIOWrapper(subprocess.Popen(["xzcat"], 
                                      stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE).stdout)
</code>
4. Use a module that wraps the <code>xz</code> command line tool
This is basically the same as the previous option, except that it's a bit more convenient and abstracts away the details.
<code>import lzma

f = lzma.LZMAFile("myfile.txt.xz", "r")
</code>

