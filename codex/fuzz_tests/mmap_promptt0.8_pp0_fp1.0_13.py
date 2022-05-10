import mmap
# Test mmap.mmap()
# 0: 文件指针，1: 索引长度，2: 文件打开模式（0:只读  1:可读写）， 3: 文件映射的类型（0:实际文件数据， 1:内存映射区域）
mf = mmap.mmap(0, 45, "MMAP_FILE", 0)    # 映射文件MMAP_FILE中的前45个字节
mf.write("abcdefghijklmnopqrstuvwxyz")   # 写入26个字节
mf.seek(0)                               # 将内存中的文件指针指向首位
