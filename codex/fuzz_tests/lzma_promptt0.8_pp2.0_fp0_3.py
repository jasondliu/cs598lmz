import lzma
# Test LZMADecompressor
shutil.copyfileobj( lzma.LZMADecompressor(open('temp.dat')), open('temp.dat.decoded', 'wb'))

# Test xz
subprocess.call(['xz', '-d', 'temp.dat'])

print('Done.')
</code>

