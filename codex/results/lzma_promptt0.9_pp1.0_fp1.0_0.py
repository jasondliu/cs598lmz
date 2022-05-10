import lzma
# Test LZMADecompressor
lzd = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
import os

folder = "transformed_icd_of_dt_separated"
# folder = "transformed_icd_of_dt"

for filename in os.listdir(folder):
    print("Filename: ", filename)
    source = open(os.path.join(folder, filename), "rb")
    # source = open("icd_dt_dvd_xz_test.lzma", "rb")
    # data = lzd.decompress(source)
    
    
    for line in source:
        data = lzd.decompress(line)
    
    
    
    # lzd.lzma_format
    # lzd.file_obj_position
    # lzd.eof
    # lzd.unused_data
    # lzd.eof
    # lzd.checksum
    # data = lzd.decompress(source)

