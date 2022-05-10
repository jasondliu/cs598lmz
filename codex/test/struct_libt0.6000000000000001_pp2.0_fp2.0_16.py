import _struct

# Load the bitmap file
f = open('bitmap.bmp','rb')

# Read the bitmap file
data = f.read()

# Close the file
f.close()

# Unpack the bitmap file
biSize, biWidth, biHeight, biPlanes, biBitCount, biCompression, biSizeImage, biXPelsPerMeter, biYPelsPerMeter, biClrUsed, biClrImportant = _struct.unpack('<IiiHHIIIIII', data[14:14+40])

# Print the bitmap file information
