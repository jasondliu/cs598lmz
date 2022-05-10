from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_XZ).decompress(xz_dat)
!echo "This is the original text" | xz > new.xz
!xz -d new.xz

# !xz -d "./human.txt.xz"
# !xz -df human.txt.xz --robot
# !cat human.txt
# !lzma decompress --format=xz --stdout human.txt.xz
# !lzma -d "./human.txt.xz"
# for file in ./human.txt.xz; do xz -d "$file"; done

# !xz -d human.txt.xz -k
!lzma -d "./human.txt.xz"
# !xz -d human.txt.xz
# subprocess.call(["xz", "-d", "human.txt.xz"])
# !tar -xf human.txt.xz -J
# !xz -d human.txt.xz
# !xz -d human.txt.xz

