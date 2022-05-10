import bz2
# Test BZ2Decompressor by decompressing all files of a bzip2
# compressed tar archive.
decompressor = bz2.BZ2Decompressor()
p = subprocess.Popen(['tar', '-tjf'],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE)
output = p.communicate(input=open('file.tbz2',
                                  'rb').read())[0]
for name in output.split(b'\n'):
    if not name:
        continue
    print(name)
    if not name.endswith(b'/'):
        filename = name
        f = open(filename, 'wb')
        bz2f = bz2.BZ2File('file.tbz2', 'rb')
        while True:
            uncompressed = decompressor.decompress(bz2f.read(100000))
            if not uncompressed:
                break
            f.write(uncompressed)
        f.close()
        os.system('diff %s %s' % (filename
