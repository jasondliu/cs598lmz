import bz2
bz2.decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

#Use the zipfile module to extract the file from the .zip archive.
import zipfile
zipfile.ZipFile('channel.zip').extractall('some_directory')

# The zipfile module can handle ZIP files that use ZIP64 extensions when the size of members 
# is larger than 4 GiB.

#Use the zipfile module to open the file readme.txt in the zipfile.
readme = zipfile.ZipFile('channel.zip').read('readme.txt')

#The zipfile module defines the following exception:
zipfile.BadZipfile

#The zipfile module defines the following functions:
zipfile.is_zipfile(filename)

#The zipfile module defines the following classes:
class zip
