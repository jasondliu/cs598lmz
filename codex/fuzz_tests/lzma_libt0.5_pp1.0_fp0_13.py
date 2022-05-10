import lzma
lzma.LZMADecompressor()

# 读取数据
with lzma.open('data/enwik8.xz') as f:
    text = f.read(100)
print(text[:100])

# 构建vocab
vocab = set(text)
vocab_to_int = {c: i for i, c in enumerate(vocab)}
int_to_vocab = dict(enumerate(vocab))
encoded = np.array([vocab_to_int[c] for c in text], dtype=np.int32)
encoded[:100]

# 构建数据集
def get_batches(arr, n_seqs, n_steps):
    '''
    对已有的数组进行mini-batch分割
    '''
    batch_size = n_seqs * n_steps
    n_batches = len(arr)//batch_size

