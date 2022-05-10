import lzma
# Test LZMADecompressor
with open('/home/kupyn/data/kaggle/BengaliAI/train_image_data_0.parquet', 'rb') as f:
    lzm = lzma.LZMADecompressor()
    data = lzm.decompress(f.read())
    print(np.frombuffer(data, dtype=np.uint8))
    print(len(data))

with open('/home/kupyn/data/kaggle/BengaliAI/train_image_data_0.parquet', 'rb') as f:
    data = f.read()
    print(len(data))

df = pd.read_parquet('/home/kupyn/data/kaggle/BengaliAI/train_image_data_0.parquet')
print(df[0])

df_p = pd.read_parquet('/home/kupyn/data/kaggle/BengaliAI/train_image_data_0.parquet')
print(df_p.head(
