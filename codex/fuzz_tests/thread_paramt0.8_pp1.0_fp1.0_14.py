import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\r{0}".format(" " * 1000))).start()
sys.stdout.flush()
    
print("Loading data...")
sys.stdout.flush()

# Load vocab
vocab_file = "data/vocab.pkl"
if os.path.exists(vocab_file):
    with open(vocab_file, "rb") as f:
        word2idx, idx2word = pickle.load(f)
else:
    word2idx = {}
    idx2word = []
    for text in TEXT.vocab.itos:
        if text not in word2idx:
            word2idx[text] = len(word2idx)
            idx2word.append(text)
    with open("data/vocab.pkl", "wb") as f:
        pickle.dump([word2idx, idx2word], f)
vocab_size = len(word2idx)

# Load train and test data
if os.path.exists
