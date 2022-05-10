import lzma
lzma.open(file_name,keep_buffer=True)

#python2
import lzma
lzma.open(file_name)

#Decompress the file to the specified destination directory
lzma.decompress(file_name, destination_directory)

#Create a compressed byte array
lzma.compress(data)

#PERFORMANCE

#Compress
lzma.open(file_name, mode='w', preset=4)

#Decompress
lzma.open(file_name, mode='r')

#Processing large files
with lzma.open(file_name, mode='r') as input_file, lzma.open(file_name, mode='w') as output_file:
    for line in input_file:
        output_file.write(line)

#Split file by parts (1 file)
with lzma.open(file_name, mode='r') as input_file, lzma.open(file_name, mode='w') as output_file:
    for
