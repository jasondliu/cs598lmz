from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)
lzma_data2 = LZMADecompressor().decompress(lzma_data)
lzma_data2 = LZMADecompressor().decompress(lzma_data)
lzma_data2 = LZMADecompressor().decompress(lzma_data)
def get_runtime(filename):
    with open(filename) as fp:
        for line in fp:
            if "real" in line:
                return line
    return line

def run_command(command):
    p = Popen(command, shell=True,
              stdout=PIPE,
              stderr=STDOUT)
    output = p.communicate()
    return output[0]
command = "lzma --compress --keep --force --output test.lzma test.txt"
run_command(command)

get_runtime("time.log")

 

command = "lzma --decompress --force --keep test.txt.lzma"
