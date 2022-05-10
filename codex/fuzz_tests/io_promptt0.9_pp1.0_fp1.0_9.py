import io
# Test io.RawIOBase inheritance
assert(issubclass(classictiff.TiffFile, io.RawIOBase))
# Test io.BufferedIOBase inheritance
assert(issubclass(io.BufferedIOBase, io.RawIOBase))


# Test TiffFile constructor
t = classictiff.TiffFile("tests/tifffile.tif")


# Test TiffFile length of opened file
assert(len(t) == 2)
print("len : %d" % len(t))


# Test number of frames
assert(t.n_frames == 2)
print("t.n_frames : %d" % t.n_frames)


# Test image reader iterator
for i, im in enumerate(t):
    print("%d. size=%s shape=%s" % (i+1, im.size(), im.shape))


# Test image reader slice handler
im1 = t[0]
assert(im1.shape == (1080, 1920, 3))
print("0. size=%s shape=%s" % (im1.size(), im1.shape))


