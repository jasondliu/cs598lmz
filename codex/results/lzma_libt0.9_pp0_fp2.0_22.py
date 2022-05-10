import lzma
lzma.LZMAOptions(dict_size=2002*1024,lc=3,lp=0,pb=2,mode=lzma.MODE_NORMAL,nice_len=192,mf=lzma.MF_BT4,depth=0)

print(lzma.LZMA_OPTIONS_MAX)
lzma.lzma_end()
print(lzma._dec_init())
print(lzma.lzma_mt_stream_init())
#print(lzma.LZMA_VERSION)
#print(lzma.LZMA_VERSION_STRING)
#print(lzma.LZMA_VERSION_NUMBER)


exit(0)

# Класс эффектов работает по алгоритму конечного состояния
class Automaton:
    def __init__(self, effect_list):
