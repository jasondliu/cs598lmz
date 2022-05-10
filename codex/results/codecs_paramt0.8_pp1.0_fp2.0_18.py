import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_default_config():
    cfg = {
        'char_size': 100,
        'max_sent_length': None,
        'max_word_length': None,
        'pos_size': 0,
        'num_filters': 30,
        'window_size': 3,
        'batch_size': 30,
        'lrate': 0.01,
        'l2_reg': 1e-8,
        'train_embeddings': False,
        'optimizer': 'sgd',
        'char_encoding': 'utf8',
        'char_level': False,
        'model_saved_dir': 'saved_models',
        'dropout': 1.,
        'loss': 'softmax',
        'src_vocab': 'data/vocab.chars.txt',
        'min_count': '0'
    }
    return cfg


def get_config(path, name):
    cfg = {}
    if path is not None:
       
