import bz2
bz2.BZ2File("src/my_compressed_file.bz2", 'w').write(data)
import bz2
bz2.BZ2File("src/my_compressed_file.bz2", 'r').read()

# Compress ZIP archive
import zipfile
zipFile = zipfile.ZipFile("src/my_compressed_zip_file.zip", 'w')
zipFile.write("src/my_file.txt")
zipFile.write("src/my_other_file.txt")
zipFile.close()

# Decompress ZIP archive
import zipfile
zipFile = zipfile.ZipFile("src/my_compressed_zip_file.zip", 'r')
zipFile.extract("my_other_file.txt", "src/my_extracted_zip_file/")
zipFile.close()

# Compress TAR archive
import tarfile
tarFile = tarfile.open("src/my_compressed_tar_file.tar", 'w')
tarFile.add("src/my_file.txt")
