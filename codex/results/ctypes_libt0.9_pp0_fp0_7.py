import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

from pylab import plot,show,imshow,contour,clf,gray,hist,axis
from numpy import *

path = 'D:\DR_wvc\ImageDatabaseSiLi\Allrois'
files = os.listdir(path)

f=open('wt.dat','w')
for file in sorted(files):
    if file.endswith(".bmp"):
        print('===================')
        print('output file:',file)
        oriImage = path + '/' + file
        oriimage = imread(oriImage)

        w,h = oriimage.shape
        newimage = zeros((w,h))


        print(oriimage.shape)
        for i in range(w):
            for j in range(h):
                if (oriimage[i][j]>0):
                    newimage[i][j]=1
                else:
                    newimage[i][j]=0
        #contour(newimage) 
        #show()

