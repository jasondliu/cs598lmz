import mmap
# Test mmap.mmap()
# open bmp file for mmap, then read in model.

# This test successfully reads in and interprets all of the image data,
# but (obviously) needs to be modified to be used as a test of
# SLICER's reading and interpretation of the data.
mapfile = mmap.mmap(open('C:/Users/Robin/Documents/BMS6221/UCSF CT lung/0001-LUNG', 'rb').fileno(), 0, mmap.MAP_PRIVATE)

#  apparently, the mmap module opens the file as readonly, which means
#  that you can't do what's done in lines 39-44. Instead, update a
#  cStringIO instance.  
data = cStringIO.StringIO()
data.write(mapfile[:10])
data.write(mapfile[256:])
data.seek(0)  # return to start of file
slice_data = data.getvalue()
data.close()


# Test mmap.mmap()
#%%
# Create an mmap() instance and read the entire file

