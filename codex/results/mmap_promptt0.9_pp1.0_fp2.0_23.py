import mmap
# Test mmap.mmap() 1GB
my_mm = mmap.mmap(-1, 1000000000, tagname="m1")
my_mm.close()
print("MMAP 1GB test - SUCCESS")
# Check storage #1 - 625GB attached to VM
# Create a file
with open('laziness.word', 'w') as f:
	f.write("If I have seen further it is by standing on the shoulders of giants. - Isaac Newton")
f.close()
# Attempt to copy the file to storage
try:
	shutil.copyfile("laziness.word", "/mnt/resource/")
except:
	print("STORAGE 1 - FAILED")
else:
	print("STORAGE 1 - SUCCESS")

# Clean up - delete the file
os.remove("laziness.word")

shutil.rmtree('laziness.word')
# Check storage #2 - 228GB attached to VM
# Create a file
with open('nirvana.lyrics', 'w') as f:
	f.write("Load up on guns and bring your friends
