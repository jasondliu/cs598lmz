from lzma import LZMADecompressor
LZMADecompressor().flush()

import argparse

parser = argparse.ArgumentParser(description='Reset a binary data')
parser.add_argument('--file', help='binary file')
args = parser.parse_args()

chunk_size = 8192
extractedChunks = 0
with open(args.file, "rb") as f:
    decompressor = LZMADecompressor()
    for chunk in iter(lambda : f.read(chunk_size), b''):
        extractedChunks += 1
        try:
            data = decompressor.decompress(chunk)
            if not chunk:
                break
            sys.stdout.write(data.decode("utf-8"))
        except Exception as e:
            print("Got an exception: ", e)
            break
