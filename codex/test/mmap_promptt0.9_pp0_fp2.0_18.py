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

