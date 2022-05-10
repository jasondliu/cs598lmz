import lzma
lzma = lzma.LZMAFile(open(sys.argv[1]))

try:
    print(lzma.read().decode())
except:
    print("Unable to decompress file")



'''
import os
import sys
import gzip
import shutil

# import gzip
# f_in = open('file.txt', 'rb')
# f_out = gzip.open('file.txt.gz', 'wb')
# f_out.writelines(f_in)
# f_out.close()
# f_in.close()

# import gzip
# gzfile = gzip.open('file.txt.gz', 'rb')
# plainfile = open('file.txt', 'wb')
# plainfile.writelines(gzfile)
# gzfile.close()
# plainfile.close()


# import os
# with open('file.txt', 'rb') as f_in, gzip.open('file.txt.gz', 'wb') as f_out:
#     shutil.copy
