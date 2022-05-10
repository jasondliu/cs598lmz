import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import os
import warnings
warnings.filterwarnings("ignore")

def preprocess(dataset_name, num_steps=None, target_class=None): 
    
    # load the data
    train = pd.read_csv("data/"+dataset_name+"/train.csv", encoding="utf8")
    test = pd.read_csv("data/"+dataset_name+"/test.csv", encoding="utf8")
    
    train_char = pd.read_csv("data/"+dataset_name+"/train-char.csv", encoding="utf8")
    test_char = pd.read_csv("data/"+dataset_name+"/test-char.csv", encoding="utf8")
    if num_steps:
        train, test = train[:num_steps], test[:num_steps]
        train_char, test_char = train_char[:num_steps
