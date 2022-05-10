import lzma
lzma1=lzma.open("./0729/0729all.lzma")
data=lzma1.read()

out=open("./0729/0729all.csv",'wb')
out.write(data)
out.close
lzma1.close



import time
import lzma
lzma1=lzma.open("./0730/0730all.lzma")
data=lzma1.read()

out=open("./0730/processed_0730_all.csv",'wb')
out.write(data)
out.close
lzma1.close



import time
import lzma
lzma1=lzma.open("./0731/0731all.lzma")
data=lzma1.read()

out=open("./0731/processed_0731_all.csv",'wb')
out.write(data)
out.close
lzma1.close
