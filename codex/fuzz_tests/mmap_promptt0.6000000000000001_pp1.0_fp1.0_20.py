import mmap
# Test mmap.mmap

f = open('/etc/passwd', 'r')
m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
print(m.readline().rstrip()) # root:x:0:0:root:/root:/bin/bash
print(m.readline().rstrip()) # daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
m.seek(0)
print(m.readline().rstrip()) # root:x:0:0:root:/root:/bin/bash
m.close()

f.close()
