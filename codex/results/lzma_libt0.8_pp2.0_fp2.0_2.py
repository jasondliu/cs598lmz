import lzma
lzma.COMPRESSION_LEVEL = lzma.PRESET_EXTREME

with open("lorem.txt", "rb") as f_in, lzma.open("lorem.txt.xz", "w", preset=lzma.PRESET_EXTREME) as f_out:
    f_out.writelines(f_in)
