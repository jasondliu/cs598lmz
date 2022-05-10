import bz2
# Test BZ2Decompressor with custom buffer size 
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(data)

# In[18]:


dataset = []
file_content = data.decode()
raw_records = file_content.split("\n")

for raw_record in raw_records :
    if raw_record:
        raw_record_split = raw_record.split("\t")
        (title, body) = (raw_record_split[1], raw_record_split[4])
        dataset.append((title, body))
        
print("Number of texts extracted :", len(dataset))
print("Sample Record :\nTitle : {0}\nBody : {1}".format(dataset[0][0], dataset[0][1]))

#Reference : https://kavita-ganesan.com/extracting-keywords-from-text-tfidf/#.XuXSLchKg2w

# define stopwords
stopwords = nltk.corpus.
