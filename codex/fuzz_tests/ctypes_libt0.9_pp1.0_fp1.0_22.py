import ctypes
ctypes.CDLL('./cwrap.so')
import cwrap
pacwrap = cwrap.cwrap
pacwrap.set_palette_color(0, 0, 255, 255)
pacwrap.set_palette_color(1, 0, 128, 128)
pacwrap.set_palette_color(2, 255, 0, 255)
# Read in NCRA logo image.
logo = np.array(Image.open('fakelogo.png'))
w, h = logo.shape[0], logo.shape[1]
pl, pu = 0.04, 0.96
xl, xu = pl * w, pu * w
yl, yu = pl * h, pu * h
# Slice the NCRA logo
ncra = logo[xl:xu, yl:yu]
plt.figure(figsize=(15, 15))
plt.imshow(ncra);

ns = 4
plt.figure(figsize=(15, 1.5 * ns))
for i in range(ns):
    plt.subplot(1, ns, i
