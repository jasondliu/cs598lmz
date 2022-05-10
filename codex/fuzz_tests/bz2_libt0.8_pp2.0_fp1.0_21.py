import bz2
bz2c = bz2.BZ2Compressor()
bz2c.compress(b"hello world")
bz2c.flush()

bz2d = bz2.BZ2Compressor()
bz2d.decompress(b"hello world")

import zipfile

with zipfile.ZipFile("my_zipped_archive.zip", mode='w') as z:
    z.write("data.json", compress_type=zipfile.ZIP_DEFLATED)

import tarfile

with tarfile.open("my_zipped_archive.tar.gz", mode='w:gz') as z:
    z.add("data.json")

# Importing a module (or package)

#The import statement
# import some_package

#The from statement
# from some_package import some_module

#The from...import * statement
# from some_package import *

#The from...import statement
# from some_package import some_module, some_other_module, some_other_other_module

#Import
