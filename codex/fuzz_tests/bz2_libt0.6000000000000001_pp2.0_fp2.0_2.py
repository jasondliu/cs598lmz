import bz2
bz2_file = bz2.BZ2File("sample_file.txt.bz2", "w")
bz2_file.write("This is a file that has been compressed with bz2\n")
bz2_file.close()

bz2_file = bz2.BZ2File("sample_file.txt.bz2", "r")
file_content = bz2_file.read()
print(file_content)


# In[ ]:
