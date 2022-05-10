import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT, offset=0)
# fileno: 文件描述符
# length: 映射区域的长度
# flags: 映射对象的类型，MAP_PRIVATE、MAP_SHARED
# prot: 映射区域的保护方式，PROT_EXEC、PROT_READ、PROT_WRITE、PROT_NONE
# access: 内存区域的访问权限，ACCESS_DEFAULT、ACCESS_COPY、ACCESS_READ、ACCESS_WRITE
# offset: 文件的偏移量，可以指定从文件的
