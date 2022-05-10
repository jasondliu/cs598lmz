import codecs
codecs.open(filename, 'r',encoding='utf-8', errors='ignore')

#make dataframe from csv
#train_data = pd.read_csv(filename)


train_data = pd.read_csv(filename, encoding='mac_roman')


#train_data = pd.read_csv(filename, encoding='latin1')


#retrieving the values of the dataframe, to be used as train_data
#turn into array
#array(train_data, dtype=object)

#load a lookup file, necessary to get the words back from their index
#lookup = pd.read_csv("lookup.csv", header=None)

#see the indices
#print(train_data.index)
#see the data types
#train_data.dtypes
#see the first few lines
#train_data.head()
#determine the number of reviews (rows)
#len(train_data)
#find the mean value for each feature
#train_data.mean()
#count the number of reviews by the first author

