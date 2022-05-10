import lzma
# Test LZMADecompressor for a file

with open('enwik8', 'rb') as fh:
    content = fh.read(lzma.CHECK_CRC32)

compressor = LZMADecompressor()
f = compressor.decompress(content)

print(f.decode('utf-8'))

fh.close()
subprocess.run(['ls', '-l'])
subprocess.run(['ls', '-lR'])
subprocess.run(['ls', '-l'], stdout=subprocess.DEVNULL)
subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
           universal_newlines=True)
subprocess.run(['echo', 'fefe', '>', 't
