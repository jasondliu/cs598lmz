import bz2
# Test BZ2Decompressor
from bz2 import BZ2Decompressor
from io import BytesIO
from xml.etree import ElementTree as ET
 
tree = ET.parse('manifest.xml')
root = tree.getroot()

debug = 0

for child in root:
  vzip = ""
  if '{http://schemas.android.com/apk/res/android}path' in child.attrib:
    vzip = child.attrib.get('{http://schemas.android.com/apk/res/android}path')
  if debug:print(vzip)
  if vzip != "":
    try:
      print(vzip)
      s = os.stat(vzip)
      vzip = bz2.open(vzip, 'rb')
      vzip_dumped = BZ2Decompressor().decompress(vzip.read())
      output = open(vzip.name[:-4],'wb')
      output.write(vzip_dumped)
      output.close()
      vzip.close()

