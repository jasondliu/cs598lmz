import bz2
bz2.BZ2File

# open the file

file1 = bz2.BZ2File('example_bz2.xml.bz2')

# read the first line

file1.readline()

# close the file

file1.close()

# print the file names

print(file1)

# read lines from the file

print(file1.readlines())

# open the file in read and write mode

file1 = bz2.BZ2File('example_bz2.xml.bz2','w')

# write to the file

file1.write(b'This is the content to write')

# close the file

file1.close()

# open the file in append mode

file1 = bz2.BZ2File('example_bz2.xml.bz2','a')

# write to the file

file1.write(b'This is the new content to write in append mode')

# close the file

file1.close()

# open the file
