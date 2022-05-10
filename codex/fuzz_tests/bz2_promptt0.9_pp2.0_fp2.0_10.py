import bz2
# Test BZ2Decompressor
#decompressor = bz2.BZ2Decompressor()
#n = decompressor.decompress(data)
#print(n)

with gzip.open('/home/zach/Downloads/rtreviews.tar.gz', 'rt') as f:
    review = ''
    for line in f.readlines():
        line = line.decode('UTF-8')
        if line.startswith('review_text:'):
            review = line
            continue
        elif line.startswith('review/time:'):
            review += ' ' + line
            print(review)
            parse(review)
        else: continue

# TODO: fix date parsing
# TODO: write to csv
