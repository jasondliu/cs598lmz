import bz2
bz2_file = "../ds4/17-32-32-66-static.rdns.colocationamerica.com-access-log.bz2"
bz2_decompressed = list()
bz2_decompressed[0] = bz2.BZ2File(bz2_file).readlines()
for i in range(1, len(bz2_decompressed[0]), 2):
    bz2_decompressed.append(bz2_decompressed[0][i])
bz2_decompressed = ''.join(bz2_decompressed)

biz2_text = bz2_decompressed.splitlines()

biz2_df = pd.DataFrame()

for i in range(0, biz2_df.shape[0]):
    biz2_df.ix[i] = biz2_text[i].split(' ')
    
del biz2_text
del biz2_decompressed

biz2_df.columns = ['unknown_1', 'unknown
