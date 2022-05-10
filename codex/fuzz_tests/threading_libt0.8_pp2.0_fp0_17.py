import threading
threading.stack_size(67108864)

# get env input
training_set = sys.argv[1]
output_file = sys.argv[2]

# parse training file
df = pd.read_csv(training_set, encoding = "ISO-8859-1", names = ["ItemID", "Sentiment", "SentimentSource", "SentimentText"])

# convert to lower case
df["SentimentText"] = df.apply(lambda row: row["SentimentText"].lower(), axis = 1)

# convert to list of strings
sentiments = df["SentimentText"].values.tolist()

# filter only the numbers
numbers = filter(isNumber, sentiments)

# convert to a sentence
numbers = list(numbers)

# strip the punctuation
for i in range(len(numbers)):
    numbers[i] = numbers[i].translate(str.maketrans('','',string.punctuation))

# tokenize the sentence
numbers = [number.split() for number in numbers]

