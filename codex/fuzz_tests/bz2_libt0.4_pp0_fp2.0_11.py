import bz2
bz2_file = bz2.BZ2File('example.bz2')
data = bz2_file.read()
bz2_file.close()

# Reading and Writing Compressed Data
import gzip
with gzip.open('example.gz', 'rt') as input_file:
    print(input_file.read())

with gzip.open('example.gz', 'wt', compresslevel=5) as output_file:
    output_file.write(data)

# Reading and Writing ZIP Archives
import zipfile
with zipfile.ZipFile('example.zip', 'r') as input_zip:
    print(input_zip.namelist())
    spam_info = input_zip.getinfo('spam.txt')
    print(spam_info.file_size)
    print(spam_info.compress_size)
    print('Compressed file is %sx smaller!' % (round(spam_info.file_size / spam_info.compress_size, 2)))
    input_zip.extractall('example')

with
