import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
# end of fix for keyboard interrupt

file_name = './data/raw_data.json'

with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f)

# set random seed
np.random.seed(42)

# split data into training and testing
train_data, test_data = train_test_split(data, test_size=0.2)

# save training data
with open('./data/train_data.json', 'w') as f:
    json.dump(train_data, f)

# save testing data
with open('./data/test_data.json', 'w') as f:
    json.dump(test_data, f)

print("Done")
