from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# lzma.LZMAError: Input format not supported by decoder
</code>
I tried to use <code>xz</code> to decompress it, but it didn't work either.
<code>import subprocess
subprocess.run(['xz', '-d', '-c', '-k', '-v', '-T0', '-f', '-9', '-e', '-0', '-S', '', '-', '-o', '-'], input=data)

# xz: (stdin): File format not recognized
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt
# xz: (stdin): Compressed data is corrupt

