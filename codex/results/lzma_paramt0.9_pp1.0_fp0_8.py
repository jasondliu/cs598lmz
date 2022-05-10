from lzma import LZMADecompressor
LZMADecompressor().decompress(open(filename, "rb").read()).decode()

# compressed2.txt is: BWPIPBWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BWP(IP)BW
