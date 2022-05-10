import _struct

def write_to_file(fname, size, data):
    with open(fname, "wb") as f:
        f.write(data)

def unpack_image(img):
    return _struct.unpack('<'+'L'*(len(img)//4), img)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 {} <input_file>".format(sys.argv[0]))
        sys.exit(1)

    with open(sys.argv[1], "rb") as f:
        data = f.read()

    if len(data) % 4 != 0:
        print("Input file is not a multiple of 4 bytes")
        sys.exit(1)

    img = unpack_image(data)

    # read the first 4 bytes, which will tell us the total number of images
    num_images = img[0]
    # and the rest of the first 4 bytes is the offset for the next image
    cur_offset = img[1]

    image
