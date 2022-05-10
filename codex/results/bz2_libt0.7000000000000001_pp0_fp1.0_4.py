import bz2
bz2.BZ2File(path_to_bz2_file, 'r')
</code>
<blockquote>
<p>OSError: [Errno 22] Invalid argument: '/Users/me/path/to/file.bz2'</p>
</blockquote>
I was able to open the same file in a different directory successfully. I have no idea what's wrong with the path. 
I also tried using zipfile:
<code>zipfile.ZipFile(path_to_bz2_file, 'r')
</code>
<blockquote>
<p>BadZipFile: File is not a zip file</p>
</blockquote>
Any thoughts on what I'm doing wrong?

