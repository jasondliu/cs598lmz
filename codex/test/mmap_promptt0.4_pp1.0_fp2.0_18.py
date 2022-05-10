import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# fileno: 一个打开的文件描述符
# length: 映射区域的长度，以字节为单位。
# flags: 控制映射区域的行为，可以是以下值的组合：
#   mmap.MAP_SHARED  该区域可以被其他进程共享
#   mmap.MAP_PRIVATE 该区域只能被当前进程访问
#   mmap.MAP_ANONYMOUS 匿名映射，与文件系统无
