from bz2 import BZ2Decompressor
BZ2Decompressor()

# Load the data.
with bz2.open('data.json.bz2', 'rb') as f:
    data = f.read().decode('utf-8')

# Load the compressed JSON data into a Python list.
data = json.loads(data)

# Print a few records.
pprint(data[0])

# Create a new DataFrame from the original JSON data.
df = pd.DataFrame(data)

# Display a few records.
df.head()

# Display the index.
df.index

# Display the columns.
df.columns

# Sort the DataFrame by the "views" column, in descending order.
df_sorted = df.sort_values(by='views', ascending=False)

# Display a few records.
df_sorted.head()

# Display the DataFrame index.
df_sorted.index

# Save the sorted DataFrame as a CSV file.
df_sorted.to_csv('sorted_data.csv')

# Create a DataFrame from the CSV file.
