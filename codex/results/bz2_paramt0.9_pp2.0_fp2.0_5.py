from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(r.content)
</code>
The third line raises a <code>ValueError</code>:
<blockquote>
<p>ValueError: data incomplete, at least 11 bytes expected, 28
  received</p>
</blockquote>
It looks like it start being uncompressed and then it just stops.
I use that script with other website and it works...
I think it's an issue with the web site, but I don't know which one.
What's wrong and how can I fix it ?


A:

You need to decompress the whole file at once, not in parts.
<code>import requests
from bz2 import BZ2Decompressor


def bz2_download(url):
    r = requests.get(url)
    decompressor = BZ2Decompressor()
    file_contents = decompressor.decompress(r.content)
    decompressor.flush()
    return file_contents


if __name__ == '__main__':
    print(bz2_download('https://kenpom.com/xls.php
