import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
# Load the dataset
data = pd.read_csv("train.csv", index_col=0)
# Preview the first 5 lines of the loaded data 
data.head()

target = data['Survived'].values
data = data.drop('Survived', axis=1)
data_list = []
for each in data.columns:
    data_list.append(data[each].values)
data = np.array(data_list)
data = data.T
# data_test = pd.read_csv("test.csv", index_col=0)
# data_test = data_test.values
# print(data_test.shape)
# print(data.shape)
# print(target.shape)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)

# print(X_train.
