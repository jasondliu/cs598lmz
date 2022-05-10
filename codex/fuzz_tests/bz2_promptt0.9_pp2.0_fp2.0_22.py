import bz2
# Test BZ2Decompressor
print("Testing...")
a = bz2.BZ2Decompressor()
end = ""
with open("result", "w") as f:
    f.write(a.decompress(b"BZh91AY&SY"))
    f.write(end)

with open("result", "r") as f:
    l = f.readlines()
    print(l)
    if l == ["BZh91AY&SY"]:
        print("OK")
    else:
        print("ERROR")
