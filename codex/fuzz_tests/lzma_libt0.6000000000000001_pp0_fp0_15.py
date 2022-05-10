import lzma
lzma.decompress(data)
</code>
It will give an error:
<code>ValueError: Error -3 while decompressing data: invalid distance too far back
</code>
I've also tried the solution here: https://stackoverflow.com/a/35984453/2576208
<code>import lzma
import io

data_io = io.BytesIO(data)
lzma.decompress(data_io)
</code>
It will give an error:
<code>ValueError: Error -3 while decompressing data: invalid distance too far back
</code>
I've tried to use <code>backports.lzma</code> and it works, but it is a backport and I don't want to use it.
Is there any other way to solve this problem?

