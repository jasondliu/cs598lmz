import bz2
# Test BZ2Decompressor by reading a file
with bz2.BZ2File('../data/amazon_reviews.bz2') as raw_data:
    with bz2.BZ2File('../data/amazon_reviews_copy.bz2', 'w') as copy_data:
        for line in raw_data:
            copy_data.write(line)
# Test BZ2Decompressor by reading a file
with bz2.BZ2File('../data/amazon_reviews.bz2') as raw_data:
    print('raw_data is {} bytes'.format(len(raw_data.read())))
    
with open('../data/amazon_reviews_copy.bz2', 'rb') as copy_data:
    print('copy_data is {} bytes'.format(len(copy_data.read())))

with gzip.open('../data/amazon_reviews.gz') as raw_data:
    print('raw_data is {} bytes'.format(len(raw_data.read())))

with open('../data/amazon_reviews_
