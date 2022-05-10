import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# 'cp65001' codec can't decode byte 0x81 in position 603: illegal multibyte 
# sequence 

# Load the data
#data = pd.read_csv('dat/dataset_shuffled.csv')
#data = data.loc[data['domain_id'] == 2]
#data = data.loc[data['elementary_school_id'] == 23]

#data = data.iloc[:10]
data = pd.read_csv('dat/dataset_shuffled.csv')

#data_1 = pd.read_csv('dat/dataset_shuffled.csv')
data_1 = data.loc[data['domain_id'] == 2]
data_1 = data_1.loc[data['elementary_school_id'] == 23]
print(data_1.shape)
#data_1 = data_1.iloc[:10]

#data
