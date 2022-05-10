import lzma
lzma.CHUNK_SIZE = (2**20) * 2
fr = gzip.open('./input/train.json.gz','rb')
df_train = pd.read_json(fr,orient='columns')
fr.close()

fr = gzip.open('./input/test.json.gz','rb')
df_test = pd.read_json(fr,orient='columns')
fr.close()
del fr


# # Pre-Processing

# In[2]:

def get_length(text):
    try:
        return len(text.split())
    except:
        print(text)
        return 0
    
def get_user_unigram(line,out,is_train=True):
    line_dict = json.loads(line)
    if is_train==True: out[0] += ' '+line_dict['description']
    out[1] += ' '+line_dict['description']
    if is_train==True: out[0] += ' '+line_dict['name']

