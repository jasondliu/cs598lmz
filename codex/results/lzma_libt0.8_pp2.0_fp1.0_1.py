import lzma
lzma.open('new.txt.xz').read()

#9-7
import sys
import os
import shutil

#9-8
import time
time.sleep(2)
time.sleep(0.5)

#9-9
import os
import shutil

time.sleep(1)
time.sleep(1)

shutil.unpack_archive('new.txt.xz', '.', 'zip')

time.sleep(1)
time.sleep(1)

time.sleep(1)
time.sleep(1)

shutil.unpack_archive('new.txt.xz.001', '.', 'zip')

time.sleep(1)
time.sleep(1)

time.sleep(1)
time.sleep(1)

#9-10
import time
time.sleep(2)
time.sleep(0.5)

#9-11
import time
import zipfile
import shutil

zip_ref = zipfile.ZipFile('a.zip', 'r')
zip_ref
