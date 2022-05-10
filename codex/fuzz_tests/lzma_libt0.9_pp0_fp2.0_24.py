import lzma
lzma.decompress("\xFD".encode("utf-8"))

print("-"*90)


import os

with open("/Users/myang/Development/python_coding_workspace/python-crash-course/8-file-io/lorem_ipsum.txt", "r") as file:
# with open("/Users/myang/Development/python_coding_workspace/python-crash-course/8-file-io/lorem_improsit.txt", "r") as file:
    print(file)
    print("File readable: {}".format(file.readable()))
    print("File closed: {}".format(file.closed))
    print("File mode: {}".format(file.mode))
    print("File name: {}".format(file.name))
    file_content = file.read()
    print("content")
    print(file_content)


print("-"*90)
print("readline()")
with open("/Users/myang/Development/python_coding_workspace/python-crash
