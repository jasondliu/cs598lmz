import bz2
bz2.decompress(file_contents)

# Read the data as a json object
import json
data = json.loads(file_contents)

# Isolate the movie information
import pandas as pd
movie_data = pd.DataFrame(data['movies'])

# Load and explore the data
print(movie_data.head())
print(movie_data.info())

# Access the data within user_ratings
user_ratings = data["ratings"]
print(user_ratings[0])

# Load and explore the data
print(pd.DataFrame(user_ratings).head())
print(pd.DataFrame(user_ratings).info())

# Apply the json_normalize function
from pandas.io.json import json_normalize

# Apply json_normalize to the 'movies' section of the data
movies_normalized = json_normalize(data, record_path='movies', meta=['user_id', 'age', 'occupation', 'zip'])

# Print the first 5 rows
print(m
