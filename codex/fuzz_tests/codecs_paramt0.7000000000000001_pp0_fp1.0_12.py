import codecs
codecs.register_error('strict', codecs.ignore_errors)


def clean_file(file_in, file_out):
    """
    Cleanup the file by removing unwanted characters and making the text
    consistent.
    """
    # This will read in the file, removing any unwanted characters
    with codecs.open(file_in, 'r', 'utf-8', 'replace') as f_in:
        text = f_in.read()

    # This will create a list of sentences, splitting on new lines
    sentences = text.split("\n")

    # This will create a list of words, splitting on spaces
    words = []

    for sentence in sentences:
        if sentence.strip():
            words.append("<s>")
            words.extend(sentence.split())
            words.append("</s>")

    # This removes any empty strings
    words = [word.strip() for word in words if word.strip()]

    # This will write the file out
    with codecs.open(file_out, 'w', 'utf-8') as f_out:
       
