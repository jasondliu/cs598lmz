import mmap
import os

#open the file
f = open('/tmp/readlines.txt')
#open the file in read mode
f = open('/tmp/readlines.txt', 'r')
#write mode
f = open('/tmp/readlines.txt', 'w')
#append mode
f = open('/tmp/readlines.txt', 'a')
#binary read mode
f = open('/tmp/readlines.txt', 'r')
#binary write mode
f = open('/tmp/readlines.txt', 'w')
#binary write mode
f = open('/tmp/readlines.txt', 'wb')

#create a file and open it in write mode.
f = open('/tmp/writelines.txt', 'w')
f.write('This is line %d\r\n' % (i+1))

#open the file and read a line
f = open('/tmp/readlines.txt', 'r')
f.readline()

#read 10 bytes
f.read(10)

#read all the lines in the file

