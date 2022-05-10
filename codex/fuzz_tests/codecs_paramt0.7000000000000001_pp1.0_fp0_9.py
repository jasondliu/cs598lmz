import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

#Read in fields
fields = []
with open(args.fields, 'r') as inFile:
    for line in inFile:
        fields.append(line.strip())

fields.append("is_toxic")

#Read in stopwords
stopwords = []
with open(args.stopwords, 'r') as inFile:
    for line in inFile:
        stopwords.append(line.strip())

#Load in vocab
vocab = {}
with open(args.vocab, 'r') as inFile:
    for line in inFile:
        element = line.strip().split("\t")
        vocab[element[0]] = int(element[1])

#Load in model
model = load_model(args.model)

#Load in data
data = pd.read_csv(args.inputFile, sep='\t', names=fields, error_bad_lines=False, encoding='utf-8')
#data.dropna(inplace
