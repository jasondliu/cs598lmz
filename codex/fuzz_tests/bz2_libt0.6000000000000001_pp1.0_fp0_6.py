import bz2
bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

# 'huge'
# 'file'

# That's right, the zip file is the password.

# The magic of this method is that the zip file is a password protected
# zip file. The password is the zip file itself.

# This is a neat trick, but there is a better way.

# Using the zipfile module, we can extract all files from a zip file
# without needing to know the password.

# The extractall method takes one arg, a path to a location where you
# would like to extract the files.

# extractall requires the zipfile to be closed first.

# The zipfile module also has a namelist method that returns a list of
# all files within the zip file.

import zip
