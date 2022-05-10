import bz2
bz2_file = bz2.BZ2File(bz2_file_name, 'w')
bz2_file.write(s)
</code>
The output file is 541 bytes in size, which is the same length as the compressed string.
What am I doing wrong?
Thank you.


A:

You need to <code>close()</code> the file:
<code>&gt;&gt;&gt; bz2_file = bz2.BZ2File(bz2_file_name, 'w')
&gt;&gt;&gt; bz2_file.write(s)
&gt;&gt;&gt; bz2_file.close()
&gt;&gt;&gt; os.stat(bz2_file_name).st_size == len(s)
True
</code>
The <code>file</code> implementation has a <code>flush()</code> method defined, but the <code>BZ2File</code> implementation does not.
You don't need to close the <code>s</
