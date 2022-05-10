import mmap
# Test mmap.mmap()
#
# open only accepts byte strings.
file1 = open('/home/shivam/Desktop/MTP/Smart-Wallet-MTP/SmartWallet-Backend/Django-Backend/split_files/new_intern_input.txt', 'r')

# open for writing
file2 = open('/home/shivam/Desktop/MTP/Smart-Wallet-MTP/SmartWallet-Backend/Django-Backend/split_files/new_intern_output.txt', 'w')

# memory-map the file, size 0 means whole file
mm = mmap.mmap(file1.fileno(), 0)
# read content via standard file methods
print(mm.readline())  # prints "Hello Python!\n"

# read content via slice notation
# print mm[:5]  # prints "Hello"
# close the map
mm.close()

# close the files
file1.close()
file2.close()
