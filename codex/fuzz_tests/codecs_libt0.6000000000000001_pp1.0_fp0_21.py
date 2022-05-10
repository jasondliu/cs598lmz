import codecs
codecs.open(file_name, encoding='utf-8')

#getting all the lines from the text file
lines = [line.strip() for line in open(file_name, 'r')]

#removing empty lines from the text file
lines = [line for line in lines if line]

#creating a sentence for each line
sentences = [sent_tokenize(line) for line in lines]

#flattening the list of sentences
sentences = [item for sublist in sentences for item in sublist]

#extracting all the words from the sentences
words = [word_tokenize(sent) for sent in sentences]

#pos tagging
pos_words = [nltk.pos_tag(word) for word in words]

#chunking
grammar = r"""

NP: {<DT|PP\$>?<JJ>*<NN>}
{<NNP>+}
{<NN>+}

"""

cp = nltk.RegexpParser(grammar)

noun_phrase = []
for i in
