import bz2
bz2.decompress(compressed_data)

# bz2.compress(data)

# bz2.open(filename, mode)


# zipfile
import zipfile
zipfile.ZipFile(filename, mode)

# zipfile.ZipFile.open(filename, mode)
# zipfile.ZipFile.extract(member, path)
# zipfile.ZipFile.extractall(path)
# zipfile.ZipFile.getinfo(member)
# zipfile.ZipFile.infolist()
# zipfile.ZipFile.namelist()
# zipfile.ZipFile.printdir()
# zipfile.ZipFile.setpassword(password)
# zipfile.ZipFile.testzip()
# zipfile.ZipFile.write(filename, arcname, compress_type)

# zipfile.is_zipfile(filename)
# zipfile.ZipInfo(filename, date_time)
# zipfile.ZipInfo.filename
# zipfile.ZipInfo.date_time
# zipfile.ZipInfo.compress_type
# zipfile.ZipInfo
