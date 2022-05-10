import mmap
# Test mmap.mmap
fin = open("/home/fxh/maoyan/plus.html", "r+")
m = mmap.mmap(fin.fileno(), 0)
# text = m.readline()
# text = m.readline()
# print(text)
m.write("abcde")
m.seek(0)
print(m.readline())
print(text)
m.close()
fin.close()

# from mmap import ACCESS_COPY,ACCESS_WRITE
# m = mmap.mmap(f.fileno(), 0)
# # 只读模式
# mmap.mmap(f.fileno(), 0, access=ACCESS_COPY)
# # 只写模式
# mmap.mmap(f.fileno(), 0, access=ACCESS_WRITE)
# print(m.readline().decode("utf-8"))
# print(m.readline().decode("utf-8"))
# m.close()
# f.close()
