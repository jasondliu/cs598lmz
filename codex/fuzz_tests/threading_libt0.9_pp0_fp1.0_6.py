import threading
threading.stack_size(2**32)

d={}
l=[]

try:
    with open("novel.txt") as f:
        text2=f.read()
except IOError:     
    print "novel.txt not found"

text=text2.decode('utf-8')

import enchant

d= enchant.Dict("en_GB")
d.add("Manuel")
d.add("Manoel") 

word_freq={}
for sentence in nltk.sent_tokenize(text):
    for word in nltk.word_tokenize(sentence):
        if word not in word_freq.keys():
            word_freq[word]=1
        else:
            word_freq[word]+=1

for word in word_freq.keys():
    if word_freq[word]==1 and word_freq[word]>3 and word_freq[word]<7:
        l.append(word)
for word in l:
    if not d.check(
