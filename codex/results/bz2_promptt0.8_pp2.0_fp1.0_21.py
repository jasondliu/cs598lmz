import bz2
# Test BZ2Decompressor
with bz2.BZ2File(dest) as fp:
  with open(dest[:-4]+'_extracted', 'wb') as fd:
    print('BZ2File:')
    while True:
      block = fp.read(1024)
      if not block:
        break
      print(block)
      fd.write(block)
    fd.close()
    fp.close()
# Test BZ2Decompressor
with bz2.open(dest) as fp:
  with open(dest[:-4]+'_extracted', 'wb') as fd:
    print('BZ2File (decompressor):')
    while True:
      block = fp.read(1024)
      if not block:
        break
      print(block)
      fd.write(block)
    fd.close()
    fp.close()
# Test BZ2Decompressor
with bz2.BZ2File(dest) as fp:
  with open(dest[:-4]+'_extracted
