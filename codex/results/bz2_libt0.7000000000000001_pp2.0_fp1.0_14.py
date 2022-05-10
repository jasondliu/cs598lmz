import bz2
bz2.open('C:/Users/ashwi/Downloads/harvard_subset.zip.bz2')

# Import the pandas package
import pandas as pd
# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())

# Load the pickled bz2 file
with bz2.open('C:/Users/ashwi/Downloads/mnist_kaggle_some_rows.csv.bz2','rb') as file:
    # Load the pickled file into a DataFrame
    df = pd.read_csv(file)

    # Print the head of the DataFrame
    print(df.head())
# Import necessary modules
import pandas as pd
import numpy as np
import glob
import os


# Write
