import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_text(file):
    """
    Reads text from a file, normalizing whitespace and stripping HTML markup.
    """
    text = codecs.open(file, 'r', 'utf-8', 'strict').read()
    return re.sub(r'\s+', ' ', text)

def get_files(dir):
    """
    Returns a list of filenames for all html files in that directory.
    """
    html_files = glob.glob(dir + os.sep + '*.html')
    return html_files

def main():
    """
    This function is called when the program is run from the command line.
    """
    # Get the names of the html files in the data folder.
    files = get_files('data')

    # Open the file we will write our features to
    with open('text_features.csv', 'w') as feature_file:

        # Create a feature extractor object.
        fe = FeatureExtractor()

        # Write the feature names to the
