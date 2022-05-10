import bz2
bz2_path = "bzip2.bz2"
new_path = "bzip2.decompressed.text"
with open(new_path,"w") as new_file, bz2.BZ2File(bz2_path,"r") as bz_file:
    for line in bz_file:
        new_file.write(line)
bz_file.close()
new_file.close()
 
decompressed_size = os.path.getsize(new_path)
print("Decompressed size is {} bytes".format(decompressed_size))

with open(new_path,"rb") as new_file:
    raw_content = new_file.read()
    print(type(raw_content))
new_file.close()

decompressed_content = raw_content.decode("utf-8")
print(type(decompressed_content))
print(decompressed_content)

# Gzip
import gzip
gzip_path = "gzip.gz"
new_path = "gzip.dec
