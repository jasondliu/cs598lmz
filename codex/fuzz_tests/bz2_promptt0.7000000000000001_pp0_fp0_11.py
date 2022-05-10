import bz2
# Test BZ2Decompressor
bz2_file = bz2.BZ2File('./data/train.ft.txt.bz2')
bz2_decompresser = bz2.BZ2Decompressor()
for line in bz2_file:
    print(line)
    break
    
bz2_decompresser = bz2.BZ2Decompressor()
bz2_decompresser.decompress(line)

data = []
with bz2.BZ2File('./data/train.ft.txt.bz2', 'rb') as f:
    for line in f:
        data.append(line.decode('utf-8'))
        
train_data = pd.DataFrame(data, columns=['review'])
train_data.head()
 
# 先分割训练集
# 思路：先用正则表达式将每条评论的正
