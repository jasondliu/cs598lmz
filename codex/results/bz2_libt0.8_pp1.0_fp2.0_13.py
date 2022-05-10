import bz2
bz2_file = bz2.BZ2File('/home/mahdi/Documents/Flickr8k_Dataset/Flickr8k_text/Flickr8k.token.txt.bz2') 
#bz2_file.read()
sents=bz2_file.read().decode("utf-8")
#print(sents)
bz2_file.close()
sents_list=sents.splitlines()
#print(sents_list)
tokens=[]
for sent in sents_list:
  tokens.append(sent.split('\t')[1])
#print(tokens)
tokenizer=Tokenizer()
tokenizer.fit_on_texts(tokens)
#print(tokenizer.word_index)
token=tokenizer.texts_to_sequences(tokens)
#print(token)
X=[]
y=[]
for i in range(0,len(sents_list)):
  img_name='Flickr8k_Dataset/Flicker8k_Datas
