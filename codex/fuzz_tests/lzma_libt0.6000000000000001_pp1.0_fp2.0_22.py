import lzma
lzma.LZMAError: Not enough data for header
</code>
I can't figure out why it says that it's not enough data for the header.
Here is the code that I am running:
<code>import os
import sys
import lzma
import gzip
import shutil
import re

def decompress_file(file_name, output_dir):
    file_extension = os.path.splitext(file_name)[-1].lower()
    print("File name:", file_name)
    print("File extension:", file_extension)

    if file_extension == ".gz":
        with gzip.open(file_name, 'rb') as f_in:
            with open(output_dir + "/" + os.path.basename(file_name) + ".txt", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    elif file_extension == ".bz2":
        with bz2.BZ2File(file_name, 'rb') as f_in
