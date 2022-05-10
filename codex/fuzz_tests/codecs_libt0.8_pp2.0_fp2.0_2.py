import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)


if __name__ == '__main__':
    print "Reading data..."
    # df = pd.read_csv('comments_no_labels.csv', encoding='cp65001')
    df = pd.read_csv('comments.csv', encoding='cp65001')
    nb_rows = len(df.index)
    labels = np.array(df['label'].tolist())
    comments = np.array(df['comment'].tolist())

    print "Data loaded"

    y = np_utils.to_categorical(labels, 2)

    train_comments = comments[:nb_rows / 2]
    test_comments = comments[nb_rows / 2:]
    train_labels = y[:nb_rows / 2]
    test_labels = y[nb_rows / 2:]

    _, test_labels_int = np_utils.to_categorical([0, 1], 2).non
