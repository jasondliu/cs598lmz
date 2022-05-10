import mmap
# Test mmap.mmap()
# Create a memory mapped file where the contents are ‘a’. mmap.mmap objects 
#allow us to treat the file as if we were directly accessing the memory mapped into it!
def function_one():
    f = open("test.bin","wb")
    f.write("a")
    m = mmap.mmap(f.fileno(),0)
    print(m.read(1))
    m.close()
    f.close()

function_one()

# Test mmap.mmap()
# Now we’ll access the same memory location despite changing the underlying file.
def function_two():
    f = open("test.bin","wb")
    f.write("a")
    m = mmap.mmap(f.fileno(),0)
    f.seek(0)
    f.write("b")
    m.seek(0)
    print(m.read(1))
    m.close()
    f.close()

function_two()
