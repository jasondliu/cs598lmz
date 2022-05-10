import codecs
codecs.open("/root/Desktop/test.txt", 'r', 'utf-8')

#Accessing Files in a Directory
import os

os.path.exists("/root/Desktop/test.txt")
os.path.isfile("/root/Desktop/test.txt")
os.path.isdir("/root/Desktop/test.txt")
os.listdir("/root/Desktop/")

#Reading Files
import codecs

f = codecs.open("/root/Desktop/test.txt", 'r', 'utf-8')
print(f.readline())

for line in f:
	print(line)

f.close()

#Writing to a File
import codecs

f = codecs.open("/root/Desktop/test.txt", 'w', 'utf-8')
f.write("This is a new line")
f.close()

#Appending to a File
import codecs

f = codecs.open("/root/Desktop/test.txt", 'a', 'utf-8')
f.write("This
