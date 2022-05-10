import mmap

def main():
    # 创建内存映射
    fd = os.open('data.txt', os.O_RDWR | os.O_CREAT)
    # 将文件大小修改为10个字节
    os.ftruncate(fd, 10)
    # 内存映射文件
    m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
    # 写入字符串
    m[0:2] = b'hi'
    # 将最后一个字符修改为'k'
    m[9] = ord('k')
    # 将内容映射到文件
    m.close()
    os.close(fd)

    # 再次映射文件
    fd = os
