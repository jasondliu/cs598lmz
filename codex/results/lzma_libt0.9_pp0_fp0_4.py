import lzma
lzma.open(file, “rb”, preset=9|lzma.PRESET_EXTREME)
This example show how to open a lzma file for reading (according to the last paragraph of the “New in version 3.3” section above):

import lzma
lzma.LZMAFile(file, mode=”rb”, preset=9|lzma.PRESET_EXTREME)

--------------------------------------------------------------------------------------------------------------------------

xz -z file.txt    # 압축
xz -d file.txt.xz # 풀기
"""
"""
txt = "Titanic.txt"
with open(txt, "r") as f:
    data = f.read()
with lzma.open(txt + ".lzma", "wt") as f: # <-----
    f.write(data)
"""
"""
import lzma
#txt = "Titanic.txt"
txt = "dummy.lzma"
with lzma.open(txt, 'rt') as
