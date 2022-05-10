import mmap
# Test mmap.mmap for various buffer size
# Create text file for test purpose
test_string = "Hello Python! " * 1024 * 1024

# to save some space, you can use re-open()
# then f.truncate(mm.size())
with open("test_string.txt", "w+b") as f:
    f.write(test_string)

# open the file for mmap
with open("test_string.txt") as f:
    for buff_size in [1, 10, 100, 1024, 1024 * 1024, 1024 * 1024 * 10]:
        mm = mmap.mmap(f.fileno(), buff_size)

        assert mm[0] == "H"
        assert mm[-1] == "!"
        assert mm[0:buff_size] == test_string[0:buff_size]
        assert mm[-10:-1] == test_string[-10:-1]

        print("buff_size=%s Done." % buff_size)
 
        # close just like a file
        mm.close()

# if run this script again,
