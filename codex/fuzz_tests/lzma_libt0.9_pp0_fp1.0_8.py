import lzma
lzma_path = 'H:\\Downloads\\mehdata'
xz_path = 'H:\\Downloads\\xzdata'
for filename in os.listdir(lzma_path):
    file_size = os.path.getsize(os.path.join(lzma_path, filename))
    if filename.endswith(".xz"):
        os.rename(os.path.join(lzma_path, filename), os.path.join(xz_path, filename))
        continue
    with open(os.path.join(lzma_path, filename), "rb") as f:
        file_content = f.read()
        dec = lzma.decompress(file_content)
        print(f"Length of original file: {file_size}")
        print(f"Length of decompressed content: {len(dec)}, ratio: {len(dec)/file_size}")

## Zip without compression
import zipfile
from io import BytesIO

no_compress_zip_dir = "H:\\
