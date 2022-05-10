import codecs
codecs.open(dir_path+"/2020_SDG_data_v2.csv", 'r', encoding='utf-8', errors='ignore')

# Input the file path of where the SDG data you want to read is
# csv file
file = dir_path+"/2020_SDG_data_v2.csv"
# Reading the csv file
data = pd.read_csv(file)
# Bringing the data into a dataframe
df = pd.DataFrame(data)

# Getting the columns of the data frame and assigning a new variable
columns = df.columns

# Creating a new data frame with 2 columns: Country and Indicator,
# and assigning all the countries and indicators in the data frame
# to them
df1 = pd.DataFrame({columns[1]: df[columns[1]].unique(), columns[2]: df[columns[2]].unique()})

# Just getting the Indicator column
df2 = df1[columns[2]]

# Creating an empty list to extract only the indicators
list_of_indicators =
