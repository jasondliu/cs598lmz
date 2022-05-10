import mmap
import random
import sys
import os

try:
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
except:
    print("pip install pillow")
    sys.exit()


NR=1000    # number of rows
NC=1000    # number of columns
FONT_SIZE=1
MAX_FONTS=1
FONT_LOCATION="/Library/Fonts/"
#FONT_LOCATION="/usr/share/fonts/truetype/msttcorefonts/"

def load_fonts(dirname):
    fonts = []
    for filename in os.listdir(dirname):
        extensions = (".ttf", ".otf", ".fon")
        if filename.lower().endswith(extensions):
            fonts.append(filename)

    if(len(fonts) == 0):
        print("did not find any fonts in", dirname)
        sys.exit()
    return fonts

