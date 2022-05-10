import bz2
# Test BZ2Decompressor on the file
with open("file.bz2", 'rb') as compressed:
    decompressor = bz2.BZ2Decompressor()
    with open("file_uncompressed.txt", 'wb') as uncompressed:
        firstTimestamp = 0
        delimiter = ","
        keysToWrite = ['timestamp', 'name', 'action_timestamp', 'action_user', 'action_text']
