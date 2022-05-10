import bz2
bz2_file = bz2.BZ2File('test.txt.bz2')
bz2_file.read()
bz2.decompress(bz2_file.read())
 
# Reading a Text File Line by Line
# 
# It's often best to read data line by line - but there are a few different ways to
# do this in Python.
# 
# The easiest way to read a text file line by line is to use the for loop statement:
# 
# with open('test.txt', 'r') as input_file:
#     for line in input_file:
#         print(line)
# 
# 
# Another way to read line by line from a file is to use the readline() function. The
# readline() function reads the next characters from a file up to and including the next
# end-of-line character, and returns a string. Here's an example of how this works:
# 
# >>> with open('test.txt', 'r') as input_file:
#         line = input_file.readline()
#        
