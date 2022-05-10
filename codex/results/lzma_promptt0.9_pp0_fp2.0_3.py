import lzma
# Test LZMADecompressor class
with LZMADecompressor() as dec:
    with open("files/xz_files/test.xz", 'rb') as file:
        file_content = dec.decompress(file.read())
        print(file_content)

file_count = 0
file_folders = []
for main_folder, subfolders, filenames in os.walk("files"):
    file_folders.append(main_folder)
    for filename in filenames:
        file_count += 1

print("\n")
print("-----------------")
print("Number of Files: " + str(file_count))
print("-----------------")
print("Folders: " + str(file_folders))
print("-----------------")

images = []
documents = []
videos = []
audio_files = []
compressed_files = []
os_files = []
internet_files = []
other_files = []

for directory, subfolders, filenames in os.walk("files"):
    for filename in filenames:

