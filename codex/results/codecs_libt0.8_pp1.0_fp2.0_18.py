import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

COPY = 0
EDIT = 1

# Params
path_to_data = "../data/"
name = "wikidump_eng"
basepath = path_to_data + name + "/"
TEST = "TEST3"

basepath_logs = basepath + "logs/"
path_to_logs = basepath_logs + TEST + "/"
path_to_features = basepath + "features/"
path_to_models = basepath + "models/"
path_to_submits = basepath + "submits/"

# Features
pages = ['0', '1', '2', '3', '4']
feature_types = ['tokens', 'parts', 'tokens_no_repeat', 'parts_no_repeat']

# Models
model_list = ['SVC_LR_2', 'SVC_LR_4', 'SVC_LR_6']

#
