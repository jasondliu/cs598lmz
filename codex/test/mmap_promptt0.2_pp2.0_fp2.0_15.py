import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# fileno: 一个打开的文件描述符
# length: 映射区域的长度，以字节为单位
# flags: 可选标志，MAP_PRIVATE、MAP_SHARED、MAP_ANONYMOUS
# prot: 可选标志，PROT_READ、PROT_WRITE、PROT_EXEC
# access: 可选标志，ACCESS_DEFAULT、ACCESS_READ、ACCESS_WRITE、ACCESS_COPY
# offset: 文件的偏移量，以字节为单位

# 打开一个文件
