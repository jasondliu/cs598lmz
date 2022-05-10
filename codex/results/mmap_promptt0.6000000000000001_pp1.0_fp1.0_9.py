import mmap
# Test mmap.mmap()
# mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])
# mmap.mmap(fileno, length, flags)
#   fileno: 文件句柄
#   length: 映射长度
#   flags: 映射标志
#   prot: 映射权限
#   access: 映射方式
#   offset: 映射偏移
filename = 'C:\\Users\\Administrator\\Desktop\\TEMP\\test.txt'
with open(filename, 'r+') as f:
    # 从文件的指定偏移量开始，创建一个mmap对象
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    # 把映射指向
