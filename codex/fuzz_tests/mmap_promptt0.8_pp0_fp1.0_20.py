import mmap
# Test mmap.mmap
&gt;&gt;&gt; f = open('largefile', 'w+')
&gt;&gt;&gt; m = mmap.mmap(f.fileno(), 1048576)
&gt;&gt;&gt; m[0] = '\0'
&gt;&gt;&gt; f.write('test')
4
&gt;&gt;&gt; m[0]
't'
&gt;&gt;&gt; m[:2]
'te'
</code>
As you can see, the modifications to the mmap object are reflected in the file object and vice versa. See the documentation for mmap for more information and examples.

