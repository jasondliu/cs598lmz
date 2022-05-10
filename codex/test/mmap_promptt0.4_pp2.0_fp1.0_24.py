import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# fileno: 文件描述符
# length: 映射区域的大小，以字节为单位
# flags: 可选，控制映射区域的类型，如果未指定，则为 mmap.MAP_SHARED
# prot: 可选，控制映射区域的访问权限，如果未指定，则为 mmap.PROT_WRITE | mmap.PROT_READ
# access: 可选，控制映射区域的访问类型
