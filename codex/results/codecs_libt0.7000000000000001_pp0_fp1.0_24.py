import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Read in the data set
data = pd.read_csv(r'C:\Users\Zack\Desktop\GMU\Linguistics\LING601\assignments\final_project\sarcasm_headlines_dataset.csv')

# Create a new column that shuffles the target column
data['target_shuffled'] = data.apply(lambda x: np.random.permutation([0,1]), axis = 1)

# Create a column for the shuffled predictions
data['shuffled_pred'] = np.nan

# Create a column for the real predictions
data['real_pred'] = np.nan

# Loop through each row in the data set
for index, row in data.iterrows():
    
    # Set up the training data
    train_index = [x for x in range(len(data)) if x != index]
    train_data = data.iloc[train_index]
    test_data = data.
