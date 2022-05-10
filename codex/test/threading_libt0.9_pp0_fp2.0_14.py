import threading
threading.stack_size(67108864) # 64MB stack
sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions

import nltk
nltk.download('maxent_ne_chunker')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')

# Assign a variable to loaded JSON
jsonFile = "../../data/optimizing-recommendations-using-rfm-analysis/yelp_academic_dataset_user.json"

# Read with Pandas
df = pd.read_json(jsonFile, lines=True)

df.head(3)

#Clean any extra spaces form columns
df.columns = df.columns.str.lower().str.replace(' ', '_')
