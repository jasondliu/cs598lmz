import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    # Prepare data
    print("Loading data...")
    x_train, y_train, x_test, y_test = data_helpers.load_data()
    # Build vocabulary
    max_document_length = max([len(x.split(" ")) for x in x_train])
    vocab_processor = learn.preprocessing.VocabularyProcessor(max_document_length)
    x_train = np.array(list(vocab_processor.fit_transform(x_train)))
    x_test = np.array(list(vocab_processor.transform(x_test)))
    n_words = len(vocab_processor.vocabulary_)
    print('Total words: %d' % n_words)
    # Build model
    print("Creating Model...")
    # Training
    # ==================================================
    with tf.Graph().as_default():
        session_conf = tf.ConfigProto(
          allow_soft_placement=FLAGS.allow_soft_placement,

