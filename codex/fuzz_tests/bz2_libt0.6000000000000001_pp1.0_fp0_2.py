import bz2
bz2.BZ2File(base_dir + "train.ft.txt.bz2", 'r').readlines()[:10]

train_file = bz2.BZ2File(base_dir + "train.ft.txt.bz2")
test_file = bz2.BZ2File(base_dir + "test.ft.txt.bz2")

train_file = train_file.readlines()
test_file = test_file.readlines()

train_file = [x.decode('utf-8') for x in train_file]
test_file = [x.decode('utf-8') for x in test_file]

train_labels = [0 if x.split(' ')[0] == '__label__1' else 1 for x in train_file]
train_sentences = [x.split(' ', 1)[1][:-1].lower() for x in train_file]

for i in range(len(train_sentences)):
    train_sentences[i] = re.sub('\d','0
