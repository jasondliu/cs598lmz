from lzma import LZMADecompressor
LZMADecompressor().decompress(read_bytes("../input/test.xz"))

#test if .gz file is readable
import gzip
with gzip.open("../input/test.gz") as f:
    file_content = f.read()
print(file_content)

#test if .tar.gz file is readable
import tarfile
with tarfile.open("../input/test.tar.gz") as f:
    file_content = f.read()
print(file_content)

#test if .zip file is readable
import zipfile
with zipfile.ZipFile("../input/test.zip") as f:
    file_content = f.read()
print(file_content)

#test if .csv file is readable
import pandas as pd
df = pd.read_csv("../input/test.csv")
df.head()

#test if .json file is readable
import json
json_data = json.load(open("../input/test.json"))
print(json_data)


"""
This program is a part of lzma
