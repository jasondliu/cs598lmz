import _struct
import sys
import json
import base64
import PIL
from PIL import Image
import sys
import math

conn = httplib.HTTPConnection("127.0.0.1:3000", 3000)

if not os.path.exists('machine.dat'):
    f = open('machine.dat', 'w')
    pickle.dump([], f)
    f.close()

f = open('machine.dat')
mach_data = pickle.load(f)
f.close()

#mach_data = [{'put_data':{'machid':'1111','imageid':'0','imageucount':'11','imagesize':'1','imageval':'029d, 0a75, 0c44, 0fb2, 0a75, 4708, 0a76, 0fb2, 4651, 0c44, 0880, 0c44, 0964, 4651, 0ff2, 0668, 2bde, 0c44, 0924, 0a75, 0c44, 0fb2, 0c44, 0fb
