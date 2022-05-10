import mmap
# Test mmap.mmap()

# import mmap

# f = open("/Users/shubham.bajpai/Documents/UserData.text", "r+b")
# m = mmap.mmap(f.fileno(), 0)
# print(m.readline())  # prints "Hello Python!\n"
# print(m[6:12])  # prints "Python"
# m.seek(0)  # rewind
# m.write("h")  # modifies file contents
# m.close()
# f.close()

f = open("/Users/shubham.bajpai/Documents/UserData.text", "r+b")
m = mmap.mmap(f.fileno(), 0)
print(m.size())
print(m.seek(0))
m.write("h")  # modifies file contents
m.close()
f.close()
