from bz2 import BZ2Decompressor
BZ2Decompressor(0).compress("")
# decompress('\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')
'''

s = open('test', 'r').read()
b = 'BZh91AY&SY'

def remove_bz2(s):
    return s.replace(b,'')

# print decompress('BZh91AY&SY' * 1000)
# print remove_bz2(decompress('BZh91AY&SY' * 1000))
# print remove_bz2(decompress('BZh91AY&SY' * 1000)) == 'BZh91AY&SY' * 1000

# bz2('BZh91AY&SY' * 1000)

# print repr(remove_bz2(''.join(map(chr,range(ord('A'),ord('Z')+1)))))
# print repr(remove_bz2(''.join(map(chr,range(ord('A'),ord('A')+1)))))
