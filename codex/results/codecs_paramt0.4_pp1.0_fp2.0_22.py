import codecs
codecs.register_error('strict', codecs.ignore_errors)

def load_data(data_dir):
    """Loads the data in data_dir, returns a list of examples and a vocabulary."""
    input_file = os.path.join(data_dir, "train.txt")
    vocab_file = os.path.join(data_dir, "vocab.txt")
    tensor_file = os.path.join(data_dir, "data.npz")

    if not (gfile.Exists(vocab_file) and gfile.Exists(tensor_file)):
        print("reading text file")
        examples = read_text_file(input_file)
        print("building vocabulary")
        vocab = build_vocab(examples)
        print("writing vocab file")
        write_vocab(vocab, vocab_file)
        print("vectorizing")
        tensor = np.array(vectorize(examples, vocab))
        print("writing tensor file")
        np.savez_compressed(tensor_file, data
