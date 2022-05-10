import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Load the data
data = pd.read_csv('../data/train.csv')

# Drop the rows with missing data
data = data.dropna()

# Extract the text and labels
texts = data['comment_text'].values
labels = data[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].values

# Convert the text to lowercase
texts = [x.lower() for x in texts]

# Replace contractions with their longer forms 
texts = [contractions.fix(x) for x in texts]

# Trim extra whitespace
texts = [' '.join(x.split()) for x in texts]

# Remove numbers
texts = [re.sub(r'\d+', '', x) for x in texts]

# Remove punctuation
texts = [re.sub(r'[^\w\s]', '', x) for x in texts]

# Remove special characters
texts = [
