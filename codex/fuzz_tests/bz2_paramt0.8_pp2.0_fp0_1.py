from bz2 import BZ2Decompressor
BZ2Decompressor()
#bz2
BZ2Decompressor
#s3
get_last_modified(bucket, key)
#s3
get_last_modified(bucket='some-bucket', key='some-key')
#s3
delete_object(bucket, key)
#s3
delete_object(bucket='some-bucket', key='some-key')
#s3
list_objects(bucket='some-bucket', prefix='path/to/data/')
#s3
list_objects(bucket, prefix)
#s3
list_objects(bucket='some-bucket', prefix='path/to/data/')
#dask
get_hashes(filename)
#dask
get_hashes(filename=filename)
#dask
get_hashes(filename=filename, algorithm='md5')
#dask
get_hashes(filename=filename, algorithm='md5', blocksize=262144)
#dask
get_hashes(filename=filename, algorithm='md5', blocksize=262144, compression='gzip
