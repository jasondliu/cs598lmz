from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(with open('data/train.csv.bz2', 'rb') as f: f.read())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
NameError: name 'with' is not defined
</code>
What am I doing wrong here?


A:

<code>with open('data/train.csv.bz2', 'rb') as f: f.read()
</code>
is a context manager, and shouldn't be put inside <code>BZ2Decompressor().decompress(...)</code>. I think you want to say
<code>with open('data/train.csv.bz2', 'rb') as f:
    BZ2Decompressor().decompress(f.read())
</code>

