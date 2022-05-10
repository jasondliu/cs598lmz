import bz2
# Test BZ2Decompressor
bz = BZ2Decompressor()
dec = []
for i in np.arange(0, len(bpeData), 10**6):
    print('processiing', i)
    dec.append(bz.decompress(bpeData[i:i+10**6]))

fullDec = b''
for i in np.arange(len(dec)):
    fullDec += dec[i]
    
with open('intermediate/bpeData.decompressed.txt', 'wb') as f:
    f.write(fullDec)
# Test BZ2Compressor
bz = BZ2Compressor()
dec = []
for i in np.arange(0, len(bpeData), 10**6):
    print('processiing', i)
    dec.append(bz.compress(bpeData[i:i+10**6]))

fullDec = b''
for i in np.arange(len(dec)):
    fullDec += dec[i]
    
with open('intermediate/bpeData
