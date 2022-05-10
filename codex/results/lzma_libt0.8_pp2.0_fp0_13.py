import lzma
lzma.compress('Hi')
</code>
CODE :
<code>import tarfile
import os
import sys
import time
import lzma

#Get file size in bytes
def getFileSize(file_path):
    try:
        # Get file size
        file_size = os.path.getsize(file_path)
        return file_size

    except Exception as e:
        print (f"Error: {e}")

# Create a compressed file
def compressFile(src, dest):
    try:
        # Create a compressed file
        print(f"Creating compressed file from source : {src}")
        start_time = time.time()
        lzma.compress(src, dest)
        end_time = time.time()
        print(f'Compressed file size is {getFileSize(dest)} bytes')
        print(f'Done in {end_time - start_time} seconds')

    except Exception as e:
        print (f"Error: {e}")

# Run compressFile for each file
def run():
   
