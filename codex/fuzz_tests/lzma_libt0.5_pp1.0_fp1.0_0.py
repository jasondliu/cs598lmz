import lzma
lzma.LZMAFile(fileobj=open('test.xz', 'rb'))
</code>
But when I try to use the same code with a large file, I get the following error:
<code>lzma.LZMAError: Input format not supported by decoder
</code>
I'm running Python 2.7.10 on OS X 10.11.3.
What am I doing wrong?

