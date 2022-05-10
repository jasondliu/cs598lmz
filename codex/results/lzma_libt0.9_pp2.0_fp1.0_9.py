import lzma
lzma_path = '../../input/train_input/train_input/train_input.csv.xz'
with lzma.open(lzma_path) as f:
    file_content = f.read()
train = pd.read_csv(f)

lzma_path = '../../input/test_input/test_input.csv.zip'
with lzma.open(lzma_path) as f:
    file_content = f.read()
test = pd.read_csv(f)
#train = pd.read_csv('../input/train.csv')
#train = train.replace(to_replace='',value=np.nan)
#test = pd.read_csv('../input/test_1.csv')
#test = test.replace(to_replace='',value=np.nan)

# Extract target (y)
y_train = train['target']
y_train = y_train.values

# Extract training features (X)
train.drop(['target','ID','v8','v
