import bz2
bz2input = bz2.BZ2File("../ftp.sec.gov/edgar/full-index/2013/QTR1/master.idx")
bz2output = bz2.BZ2File("../ftp.sec.gov/edgar/full-index/2013/QTR1/master-bz2.idx","w")
for l in bz2input:
    bz2output.write(l)
bz2output.close()
bz2input.close()

print("master.idx file compressed.")



bz2output = bz2.BZ2File("../ftp.sec.gov/edgar/full-index/2013/QTR1/master-bz2-compresslevel-9.idx","w",9)
bz2input = bz2.BZ2File("../ftp.sec.gov/edgar/full-index/2013/QTR1/master.idx")
for l in bz2input:
    bz2output.write(l)
bz2output.
