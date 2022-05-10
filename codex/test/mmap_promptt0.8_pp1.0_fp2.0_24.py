import mmap
# Test mmap.mmap(fileno,length)
# before using this test:
# touch testfile.txt
# echo "this is a test file" >> testfile.txt
# cat testfile.txt
# $python3 mmap_file.py
f = open('testfile.txt', 'r+b')
m = mmap.mmap(f.fileno(), 0)
print(m.read(10)) # Prints "this is a"
m.close()
