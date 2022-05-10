import lzma
# Test LZMADecompressor
with gzip.open('data/wikimedia/wiki-001.zst') as f, lzma.LZMADecompressor(format=lzma.FORMAT_ZSTD) as decomp:
    data = f.read()
    dec_data = decomp.decompress(data)
    with open('data/lzma/wiki-001-lzma.txt', 'wb') as res:
        res.write(dec_data)
# Stampede2
!zstd -d -f $SCRATCH/wikipedia-light-1gb.zst
# Cori
!zstd -d -f $SCRATCH/wikipedia-light-1gb.zst
 
!ls $SCRATCH/wikipedia-light-1gb.txt
# Decompress this single file on Cori
!time zstd -d -f $SCRATCH/wikipedia-light-1gb.zst

# Decompress this file on Stampede2
!time cp -r $SCRATCH/screen-1gb.zstd $TMPDIR/
!time zstd -
