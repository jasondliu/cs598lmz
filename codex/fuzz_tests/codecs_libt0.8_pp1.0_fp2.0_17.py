import codecs
codecs.open('mushrooms.csv', "r", "utf-8")

# 1. Read in the data with `read_csv()`.
mushrooms = pd.read_csv('mushrooms.csv')

# 2. Run the cell below to see what the data looks like.
mushrooms.head()

# 3. Look at the shape of the data.
mushrooms.shape

# 4. Run the cell below to see how many `False` and `True` values there are in the `mushrooms` data.
mushrooms['class'].value_counts()

# The False class has more data points, so it will be the majority class



# 5. Pick two features to use as predictors.
X = mushrooms[['odor', 'gill-color']]

# 6. Create your target variable. Remember, your target variable is the `class` column.
y = mushrooms['class']


# 7. Create a dummy variable to deal with the string values.
X = pd.get_dummies(X, drop_first=True)

# 8
