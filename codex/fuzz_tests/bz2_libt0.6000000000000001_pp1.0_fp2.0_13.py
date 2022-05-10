import bz2
bz2_file_name = 'data/numbers.bz2'

with bz2.open(bz2_file_name, 'wt') as file:
    file.write('\n'.join(numbers))
    
!ls -lh $bz2_file_name

with bz2.open(bz2_file_name, 'rt') as file:
    for line in file:
        print(line)

# compress a file
!bzip2 $bz2_file_name

# decompress a file
!bunzip2 $bz2_file_name.bz2

# compress a file and delete the original
!bzip2 -k $bz2_file_name

# compress a file using the best compression
!bzip2 -z $bz2_file_name

# decompress a file using the best compression
!bunzip2 -k $bz2_file_name.bz2

# compress multiple files
!bzip2 -z data/numbers.txt data/numbers.bz
