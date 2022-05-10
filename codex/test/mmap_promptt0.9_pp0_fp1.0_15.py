import mmap
# Test mmap.mmap()
fp = open('D:\\Tools\\Pytest\\testdata.txt', 'r+')
fp.write('0123456789abcdef')
fp.seek(0)
m = mmap.mmap(fp.fileno(), 15)
