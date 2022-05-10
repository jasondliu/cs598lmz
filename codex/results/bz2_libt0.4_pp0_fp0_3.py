import bz2
bz2.BZ2File(file_name)

# open the file with bz2
with bz2.BZ2File(file_name) as file:
    # print the file contents
    print(file.read())

# open the file with bz2
with bz2.BZ2File(file_name) as file:
    # decompress the file contents
    file_content = file.read()
    # print the file contents
    print(file_content)

# open the file with bz2
with bz2.BZ2File(file_name) as file:
    # decompress the file contents
    file_content = file.read()
    # decode the file contents
    file_content_decoded = file_content.decode('utf-8')
    # print the file contents
    print(file_content_decoded)

# open the file with bz2
with bz2.BZ2File(file_name) as file:
    # decompress the file contents
    file_content = file.read()
    # decode
