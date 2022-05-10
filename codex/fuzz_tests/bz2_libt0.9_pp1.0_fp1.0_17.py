import bz2
bz2_file=bz2.BZ2File("sponge.txt.bz2")
file=bz2_file.read()
print(file)

# 5. "raven.txt"を、0から1の範囲で分割した"raven_0_to_1.txt"、"raven_10_to_20.txt"、  
# "raven_20_to_30.txt"、...、"raven_90_to_100.txt"というファイル名で10等分保存せよ。
file=open("raven.txt","r")
con=file.read()
n10=len(con)//10+1

for i in range(10):
    file=open(f"raven_{10*i}_to_{10*i+10}.txt","w")
    file.write(con[10*i:10*i+10])
    file.close()


# 6. ディレクトリlsのなかの
