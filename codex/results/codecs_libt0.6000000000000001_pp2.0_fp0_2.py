import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Keep track of the progress of this analysis
print("Parsing the data...")

# Get the data
data = pd.read_csv("../data/raw/raw_data_project_mssm.csv")

# Remove all the rows with "N/A"
data = data.replace("N/A", np.nan)
data = data.dropna()

# Remove all the rows with "Unnamed"
data = data.loc[data['PGC'] != 'Unnamed: 0']

# Convert the PGC column to int
data['PGC'] = data['PGC'].astype('int64')

# Print out the amount of rows
print("The amount of rows is " + str(len(data)))

# Print out the amount of data
print("The amount of columns is " + str(len(data.columns)))

# Print out the data
print(data)

# Print out the progress
print("Data has been
