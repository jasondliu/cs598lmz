import mmap
# Test mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_READ|PROT_WRITE, access=ACCESS_DEFAULT, offset=0)
# 创建映射，分配一块内存
# fileno: 文件描述符
# length: 映射的字节数
# flags: 内存的读写属性
# prot: 内存的可访问属性
# access: 内存的可访问模式
# offset: 访问文件的偏移量
# 可以用来操作文件的一部分，而不用读取整个文件
# mmap实例的方法
# mmap.close()
#
