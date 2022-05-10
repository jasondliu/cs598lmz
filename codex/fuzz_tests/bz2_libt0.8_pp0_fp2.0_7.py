import bz2
bz2.BZ2File( filename )

#file_handle = open( filename, 'rb' )
#bz_file_handle = bz2.BZ2File( file_handle )

#for line in bz_file_handle.readlines():
#    print line.strip()

#import bz2
#file_handle = open( filename, 'rb' )
#bz_file_handle = bz2.BZ2File( file_handle, 'r' )
#print bz_file_handle.readline().strip()

#import gzip
#file_handle = open( filename, 'rb' )
#gz_file_handle = gzip.GzipFile( file_handle )
#print gz_file_handle.readline()

#import gzip
#with gzip.open( filename, 'rb' ) as gz_file_handle:
#    print gz_file_handle.readline()

#import tarfile
#file_handle = tarfile.open( filename, 'r')
#for file_obj in file
