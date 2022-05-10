from bz2 import BZ2Decompressor
BZ2Decompressor.MAX_WBITS=23
print("Loading training data")
X_train = []
Y_train = []
for line in BZ2File("train.ft.txt.bz2"):
    label, sentence = line.decode("utf-8").split(" ", 1)
    #print(line.decode("utf-8"))
    X_train.append(basic_tokenizer(sentence))
    Y_train.append(int(label))
    
X_train[100],Y_train[100]

pad_word = "<pad>"
stopwords = "the her him that this and it to of a in on at is his but with for be as i your have just not do from this are was or all so an by if he into has more no she when one his very can out all also after get me new our how people many other like even then any way see between other same first use must some through still such which who these has our by she all made"
stopwords = stopwords.split()

print("Loaded training data")

X_test = []
Y_test = []
for
