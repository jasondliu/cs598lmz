import bz2
bz2.open('file.bz2', 'rb')

# Open a gz file
import gzip
gzip.open('file.gz', 'rb')

# Custom openers
import tarfile
from contextlib import closing
f = tarfile.open('file.tar.gz')
with closing(f) as tfile:
    for member in tfile.getmembers():
        print member.name
        tfile.extract(member.name)

# Open image files
# Image is also a file
from PIL import Image
from PIL.ExifTags import TAGS

def exifinfo(img):
    # Print out exif information in img
    ret = {}
    i = Image.open(img)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

exifinfo('image.jpg')
