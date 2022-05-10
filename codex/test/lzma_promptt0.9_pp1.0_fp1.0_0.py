import lzma
# Test LZMADecompressor
lzd = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
import os

folder = "transformed_icd_of_dt_separated"
# folder = "transformed_icd_of_dt"

