import bz2
bz2.decompress(foo)
</code>
or
<code>import bz2
bz2.decompress(foo).decode('utf-8')
</code>
Also this works:
<code>bz2.decompress(foo).decode('utf-8').replace('\n', '')
</code>

