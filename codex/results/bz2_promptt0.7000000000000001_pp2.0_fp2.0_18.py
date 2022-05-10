import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

#with bz2.BZ2File('data/mr_fancy_pants_bz.json.bz2', 'r') as infile, open('data/mr_fancy_pants_bz.json', 'w') as outfile:
with bz2.BZ2File('data/mr_fancy_pants_bz.json.bz2', 'r') as infile: #, open('data/mr_fancy_pants_bz.json', 'w') as outfile:
    for data in iter(lambda: infile.read(100 * 1024), b''):
        decompressed_data = decompressor.decompress(data)
        #outfile.write(decompressed_data)
        print(decompressed_data)

# https://stackoverflow.com/questions/22275572/how-to-read-a-bz2-file-in-python-3
import bz2
# Test BZ2Decompressor
decompressor =
