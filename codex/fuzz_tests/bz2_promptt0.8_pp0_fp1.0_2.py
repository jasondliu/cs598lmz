import bz2
# Test BZ2Decompressor
decompressor = BZ2Decompressor()
with open('files_to_test/sample_1.bz2', 'rb') as file_obj:
    chunk = file_obj.read(100)
    print(decompressor.decompress(chunk))
    while True:
        chunk = file_obj.read(100)
        if not len(chunk):
            break
        print(decompressor.decompress(chunk, True))
with open('files_to_test/sample_2.bz2', 'r') as file_obj:
    print(file_obj.read())
with bz2.open('files_to_test/sample_1.bz2', 'rt') as file_obj:
    print(file_obj.read())
with bz2.open('files_to_test/sample_2.bz2', 'rt') as file_obj:
    print(file_obj.read())
 
with bz2.open('files_to_test/sample_3.bz2', 'r', encoding='
