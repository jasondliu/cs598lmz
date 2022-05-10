from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

c = open('decompressed.txt.bz2', 'rb')
compressed = c.read()
decompressed = BZ2Decompressor().decompress(compressed)

string = str(decompressed)
string = string.replace("\\n", "")

print("\n" + string)

compressed.decode("utf-8")

d = open('decompressed.txt', 'w')

d.write(string)
d.close()
</code>


A:

<code>&gt;&gt;&gt; with open('big.txt.bz2', 'rb') as c, open('big.txt', 'wb') as d, bz2.BZ2Decompressor() as decompress:
...     text = decompress.decompress(c.read())
...     d.write(text)
... 
&gt;&gt;&gt; with open('big.txt') as e, open('big-actual.txt') as f:
...     print(
