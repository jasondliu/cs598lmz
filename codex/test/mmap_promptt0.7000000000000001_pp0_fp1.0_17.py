import mmap
# Test mmap.mmap
with open('/tmp/foo','wb+') as f:
    mm=mmap.mmap(f.fileno(),0)
    mm.write('hello, python\n')
    mm[:5]='bye'
