import lzma
lzma.LZMADecompressor.decompress

import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: lzma_extract.py file")
        return

    fn = sys.argv[1]
    with open(fn, 'rb') as f:
        data = f.read()

    if len(data) < 2 or data[0:2] != b'\xfd7z':
        print("Invalid file")
        return

    #print("Header Length:", data[2])
    #print("Archive Version:", data[3])
    #print("Start Header CRC:", data[4:6])
    #print("Archive Start Header:", data[6])

    #print("\nStart Header Fields:")
    #print("Archive Properties:", data[7:11])
    #print("Additional Start Header Size:", data[11])
    #print("Additional Start Header Data:", data[12:12+data[11]])
    #print("Start Pos:", 12+
