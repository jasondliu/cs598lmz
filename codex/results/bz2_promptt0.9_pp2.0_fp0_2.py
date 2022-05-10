import bz2
# Test BZ2Decompressor class
decomp = bz2.decompressor()

os.chdir('../python/bz2-dec')
fin_bz2 = open('US.bz2', 'rb')
fin_txt = open('us_cities.vcalc', 'wb')

dat_bz2 = fin_bz2.read()
dat_txt = decomp.decompress(dat_bz2)

fin_bz2.close()
fin_txt.write(dat_txt)
fin_txt.close()
os.chdir('../../')
import bz2
os.chdir('../python')

print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
os.chdir('../')



def
