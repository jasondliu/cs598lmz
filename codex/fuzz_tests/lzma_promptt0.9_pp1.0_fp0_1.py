import lzma
# Test LZMADecompressor
f = open(sys.argv[1], 'rb')
lz = lzma.LZMADecompressor()
while True:
    data = f.read(512)
    if not data:  # Read all data
        break
    result = lz.decompress(data)
    if result:
        sys.stdout.write(result)
    elif lz.unused_data:
        sys.stdout.write(lz.unused_data)
</code>
How to decompress the file generated with <code>subprocess.Popen()</code>?

With <code>p=subprocess.Popen(['lzma','-c','-d',sys.argv[1]],stdout=subprocess.PIPE)</code>, I've got:
<blockquote>
<p>AttributeError: 'NoneType' object has no attribute 'decompress'</p>
</blockquote>
With <code>p=subprocess.Popen(['lzma','-c','-d',sys.argv[1]]
