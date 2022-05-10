import bz2
bz2.BZ2File(filename)

# Read the file
file = bz2.BZ2File(filename)
data = file.read()

# Close the file
file.close()

# Check number of rows
len(data.split('\n'))

# Check out the first 1000 characters in data
data[:1000]

# Import necessary modules
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Create a series to store the labels: y
y = df.label

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], y, test_size=0.33, random_state=53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words='english')

# Transform the training data using only the 'text' column values: count_train 
count_train = count_vectorizer.fit_transform(X_train)

# Transform the test data
