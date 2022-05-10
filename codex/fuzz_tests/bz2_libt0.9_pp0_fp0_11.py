import bz2
bz2_file =  bz2.BZ2File("lorem_ipsum.txt.bz2")
print("Printing file content of lorem_ipsum.txt.bz2") 
print(bz2_file.read().decode("utf-8"))
print("Closing file...")
bz2_file.close()
