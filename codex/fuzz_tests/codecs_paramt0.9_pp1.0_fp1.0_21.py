import codecs
codecs.register_error('strict', codecs.ignore_errors)

### Parametros para cada modulo

ap = argparse.ArgumentParser()

ap.add_argument('--emb', default='../../data/sensitivity/cornell-movie-corpus/word_vectors.txt', help='the embedding file in text format')
#ap.add_argument('--data', default='../../data/sensitivity/cornell-movie-corpus/processed_5class/', help='the folder containing the files for the experiment')
ap.add_argument('--data', default='../../data/sensitivity/cornell-movie-corpus/processed_5class/', help='the folder containing the files for the experiment')
ap.add_argument('--torch_model', default='../../data/sensitivity/cornell-movie-corpus/model/conversation_classifier_3la.pt', help='file where the torch model is saved')
ap.add_argument('--ann_model', default='../../data/sensitivity/cornell-movie-corpus
