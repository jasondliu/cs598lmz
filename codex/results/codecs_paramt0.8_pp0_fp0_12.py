import codecs
codecs.register_error('ignore', codecs.replace_errors)

filename = "../data/bob.txt"
data = codecs.open(filename, "r", "utf-8", "ignore").read()

data_ = "".join(dat for dat in data if dat not in exclude)

for sent in sent_detector.tokenize(data_):
    print(sent)
