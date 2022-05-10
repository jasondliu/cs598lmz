import mmap
# Test mmap.mmap
aData = "ssssss"
fObj = open("file.txt", "w")
fObj.write(aData)
fObj.flush()

#
# Test mmap.mmap(), write mode
#
fObj.close()
fObj = open("file.txt", "r")

mObj = mmap.mmap(fObj.fileno(), 0)
if mObj.find("ssss") == -1:
    print("Test 18 failed")

if mObj.find("hhh") != -1:
    print("Test 18 failed")

if mObj.find(u"ssss", "utf-8") == -1:
    print("Test 18 failed")

