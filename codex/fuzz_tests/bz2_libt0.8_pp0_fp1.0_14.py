import bz2
bz2.__version__

tmp_dir = "/tmp/"
tmp_file_name = "test.txt"
tmp_file_path = tmp_dir + tmp_file_name
tmp_bz2_file_name = tmp_file_name.replace(".txt", ".bz2")

with open(tmp_file_path, "w") as f:
    f.write("hello world")
with open(tmp_file_path, "rb") as f:
    with bz2.open(tmp_bz2_file_name, "wb") as f2:
        f2.write(f.read())
# 'rb' is interpreted as binary format
# 'wb' is interpreted as binary format
# and write the compressed file to the current directory
with open(tmp_bz2_file_name, "rb") as f:
    file_content = f.read()
file_content

with open(tmp_file_path, "rb") as f:
    file_content = f.read()
file_content

# compress the file
# compress the file

