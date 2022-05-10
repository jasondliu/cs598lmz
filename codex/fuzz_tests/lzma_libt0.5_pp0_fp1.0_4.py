import lzma
lzma.open

with open('../../data/test_data/test.csv') as f:
    df = pd.read_csv(f)

print(df.head())

df.to_csv('../../data/test_data/test_out.csv')
