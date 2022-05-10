import lzma
# Test LZMADecompressor before using it. Otherwise, it will raise an error if LZMA
# is not supported on the platform.
s = b'\x00\x00\x00\x03\x00\x00\x00\x00\xecUN\x00\x88\x01\x99\x00\x16\x00\x00\x00k\xba\x1e\x1ey\xe0\xf8tA\xaa'
len(lzma.LZMADecompressor().decompress(s))

def read_str(myfile, nb):
    '''Read a string from a file object'''
    data = myfile.read(nb)
    try:
        return data.decode('utf-8')
    except UnicodeDecodeError:
        return data.decode('LATIN1')

def csv_extensions(value):
    '''Argparse type for csv file extensions'''
    for ext in value.split(','):
        if re.match(r'.*\..+', ext):

