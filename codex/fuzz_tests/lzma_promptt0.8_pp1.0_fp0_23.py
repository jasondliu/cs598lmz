import lzma
# Test LZMADecompressor
im = Image.open("/home/jsaxen/Documents/ValkyrieX/DE0_SOC/SOC_SDRAM_TEST/CAMERA_OUT/camera_out.raw")
width, height = im.size
pixels = list(im.getdata())
pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
with open("/home/jsaxen/Documents/ValkyrieX/DE0_SOC/SOC_SDRAM_TEST/CAMERA_OUT/camera_out_lzma.raw", 'rb') as f:
    data = f.read()

data = lzma.decompress(data)
scaled = [int(i * 255.0) for i in data]
img = Image.new('L', (width, height))
img.putdata(scaled)
img.save('/home/jsaxen/Documents/ValkyrieX/DE0_SOC/SOC_SDRAM_TEST/CAMERA_OUT/camera_out_l
