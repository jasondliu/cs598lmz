import lzma
# Test LZMADecompressor with a data stream
# from the Unix 'compress' command.

d = lzma.LZMADecompressor()

with open('dump.xz', 'rb') as f:
    for chunk in iter(lambda : f.read(256 * 1024), b''):
        outdata = d.decompress(chunk)
        print(outdata)
    outdata = d.flush()
    print(outdata)

print('Finished')
</code>
The file is around 2.5G, so reading it in 1 piece is not an option. (That's why I'm using a generator)
The problem is that it doesn't finish printing until the input file has been fully read.
The output file should be printed, but it is printed at the very end of the process.
I guess it is because of the buffer size, but I was wondering what is the correct way to do it, or if there is a better way apart from <code>lzma</code>.


A:

You could try to use the <code>pipe</code> functionality.
<code>import lzma
