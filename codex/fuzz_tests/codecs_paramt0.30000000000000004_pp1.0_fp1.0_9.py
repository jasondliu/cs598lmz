import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load the data
data = pd.read_csv('../data/train.csv', encoding='utf-8', errors='replace_with_space')

# Extract the labels
labels = data.sentiment.values

# Extract the reviews
reviews = data.review.values

# Print the first label and review
print(labels[0])
print(reviews[0])

# Create a new list of reviews
new_reviews = []

# For each review in the data
for review in reviews:
    # Append the clean review to the new list
    new_reviews.append(clean_text(review))

# Print the first cleaned review
print(new_reviews[0])

# Create a new list of labels
new_labels = []

# For each label in the data
for label in labels:
    # If the label is 0, append 0
    if label == 0:
        new_labels.append(0)
    # Else, append 1
    else:
