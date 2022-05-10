import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_folds(file_path, num_folds=5, seed=42):
    with open(file_path, 'r', encoding='utf-8') as file:
        random.seed(seed)
        data = [line.strip("\n") for line in file.readlines() if len(line.strip("\n")) > 0]
        random.shuffle(data)
        folds = [data[i:i + len(data) // num_folds] for i in range(0, len(data), len(data) // num_folds)]
        for i in range(len(folds)):
            random.shuffle(folds[i])
        return folds


def generate_folds(src_data_path, target_data_path, num_folds=5, seed=42):
    src_files = [f for f in listdir(src_data_path) if isfile(join(src_data_path, f))]
    target_files = [f for f in listdir(
