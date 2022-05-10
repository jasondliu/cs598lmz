import lzma
lzma.check_is_supported()

import sys

if len(sys.argv) != 2:
  print("Invalid number of arguments: you called '%s'" % sys.argv[0])
  print("with %d arguments instead one:" % (len(sys.argv)-1))
  print("  python %s <pack name>" % sys.argv[0])
  sys.exit(0)
  
# ~ exit()

file_name = sys.argv[1]

data_file = open(file_name, 'rb')
data = data_file.read()
data_file.close()

# Decompress the file

file_name_decompressed = file_name.split('.')[0]

if file_name_decompressed.endswith('pack'):
  file_name_decompressed = file_name_decompressed[:-4]

file_name_decompressed += '_decompressed'

print("Decompressing '%s' to '%s'..." % (file_name,
