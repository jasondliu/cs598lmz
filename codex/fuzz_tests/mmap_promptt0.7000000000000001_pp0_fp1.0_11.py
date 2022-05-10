import mmap
# Test mmap.mmap
#import mmap
#
#f = open('/etc/passwd', 'r')
#m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#if m.find('root:x:0:0:root:/root:/bin/bash') != -1:
#    print 'found string in file'
#m.close()
#f.close()

def match_word(word):
    f = open('Dictionary.txt', 'r')
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if m.find(word) != -1:
        return True
    else:
        return False
    m.close()
    f.close()
