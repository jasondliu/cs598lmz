import bz2
bz2.decompress(f1) #TypeError: cannot concatenate 'str' and 'NoneType' objects  
</code>
I don't know why. The following sentence works well. I think bz2.decompress() returns str(line) ,So I can add some characters to it. so it TypeError doesn't make sense to me.
<code>#add a space to line end
for line in f:
    print bz2.decompress(line)+' ' 
</code>
how to fix it? I want to let bz2.decompress() returns str(line) directly.


A:

The <code>bz2.decompress()</code> function doesn't return any value, as stated in the documentation. Try this instead:
<code>&gt;&gt;&gt; f1 = bz2.compress("this is a test")
&gt;&gt;&gt; print bz2.decompress(f1)
this is a test
&gt;&gt;&gt; f2 = bz2.compress("this
