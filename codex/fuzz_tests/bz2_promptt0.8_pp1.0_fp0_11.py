import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('ch2.bz2', 'rb') as input, open('ch2.xml', 'wb') as output:
  while True:
    chunk = input.read(100)
    if len(chunk) == 0:
      break
    uncompressed = decompressor.decompress(chunk)
    if uncompressed:
      output.write(uncompressed)
    else:
      break
with open('ch2.xml', 'rb') as input, open('ch2.out', 'wb') as output:
  text = input.read().decode('utf-8')
  print text.count('{http://www.mediawiki.org/xml/export-0.10/}')
  print text.count('{http://www.mediawiki.org/xml/export-0.10/}page')
  print text.count('{http://www.mediawiki.org/xml/export-0.10/}title')
  print text.count('{http://www.mediawiki.org
