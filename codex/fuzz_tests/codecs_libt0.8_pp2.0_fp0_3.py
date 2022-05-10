import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# read dataset, input data file name and separator
df = pd.read_csv("pp-complete.csv", sep=",")

# print the shape of the dataset and first 5 rows
print("Shape of Dataset is:")
print(df.shape)
print(df.head())

# print general information about the dataset and types of the columns
print("\nGeneral information about the dataset:")
print(df.info())

# print the number of missing values for each column
print("\nNumber of missing values for each column:")
print(df.isnull().sum(axis = 0))

# print the number of different values for each column
print("\nNumber of different values for each column:")
for colname in df.columns:
    print("{:21}   {:3}".format(colname, df[colname].nunique()))

# show column names
print("\nColumn names:")
print(df.column
