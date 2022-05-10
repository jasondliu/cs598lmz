import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def read_songs(file_name):
    """
    Reads in a file of songs and returns a list of tuples of the form (title, artist, lyrics).

    Parameters
    ----------
    file_name : str
        The name of the file to be read in.

    Returns
    -------
    list of tuples
        A list of tuples of the form (title, artist, lyrics).
    """
    songs = []
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            songs.append((row[0], row[1], row[2]))
    return songs

def read_stopwords(stopwords_file):
    """
    Reads in a file of stopwords and returns a set of stopwords.

    Parameters
    ----------
    stopwords_file : str
        The name of the file to be read in.

    Returns
    -------
    set
        A set of stop
