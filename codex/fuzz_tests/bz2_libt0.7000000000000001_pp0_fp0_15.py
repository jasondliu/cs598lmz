import bz2
bz2.decompress(compressed_data)

import bz2
bz2.decompress(compressed_data).decode('utf-8')

import bz2
uncompressed_data=bz2.decompress(compressed_data)
text=uncompressed_data.decode('utf-8')

#Writing Files

my_file=open('output.txt', 'w')
my_file.write('this is a test\n')
my_file.close()

my_file=open('output.txt', 'w')
my_file.write('this is a test\n')
my_file.write('second line\n')
my_file.close()

my_file=open('output.txt', 'w')
my_file.write('this is a test\n')
my_file.write('second line\n')
my_file.write('third line\n')
my_file.close()

my_file=open('output.txt', 'w')
my_file.write(text)
my_
