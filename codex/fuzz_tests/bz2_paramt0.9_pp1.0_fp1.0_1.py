from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(temp6[0])
</code>


A:

You can use something like this:
<code>from bz2 import BZ2Decompressor
import django.utils.encoding

temp6[0].decode('utf-8')

BZ2Decompressor().decompress(temp6[0])
</code>
If you are still getting the same error, it might be because the file is corrupted. I would suggest you to try on some other files.

