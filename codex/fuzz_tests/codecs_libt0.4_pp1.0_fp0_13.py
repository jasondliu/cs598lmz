import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set the working directory
os.chdir('C:/Users/sarah/Desktop/Data Science/Capstone/Data')

# Import the data
train_data = pd.read_csv('train.csv', encoding = "ISO-8859-1")
test_data = pd.read_csv('test.csv', encoding = "ISO-8859-1")

# Get the shape of the data
print(train_data.shape)
print(test_data.shape)

# Check the data types
print(train_data.dtypes)
print(test_data.dtypes)

# Check the first few rows of the data
print(train_data.head())
print(test_data.head())

# Check the summary statistics of the data
print(train_data.describe())
print(test_data.describe())

# Check for missing values
print(train_data.isnull().sum())
print(test_data.is
