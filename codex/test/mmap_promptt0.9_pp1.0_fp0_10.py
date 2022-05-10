import mmap
# Test mmap.mmap() type
print(type(mmap.mmap(0, 1)))

'''
windows下文件映射
一个文件mmap实例，每次是以文件的页为单位进行映射，文件页大小固定，
在不同系统下可能会不一样。可以通过os.sysconf('SC_PAGE_SIZE')得到当前
系统的页大小。mmap模块不更新文件时间戳。
'''
import os
import mmap
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
