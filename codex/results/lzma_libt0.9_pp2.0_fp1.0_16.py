import lzma
lzma.compress(b"a" * 10)

import gzip
from io import BytesIO
filelike_object = BytesIO()
with gzip.GzipFile(fileobj=filelike_object, mode="w") as f:
    f.write(b"Hello\n")

with gzip.open("test.txt.gz", "rt") as f:
    file_content = f.read()
print(file_content)

with zipfile.ZipFile("test.zip", "w") as myzip:
    myzip.write("test.txt")

with zipfile.ZipFile("zipped_files.zip", "w") as myzip:
    for file in glob.glob("*.txt"):
        myzip.write(file)

with zipfile.ZipFile("zipped_files_single_archive.zip", "w") as zfile:
    with zfile.open("README.txt", "w") as dest:
        with open("README.txt", "rb") as source:
            shutil.copyfileobj(
