import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Download data from stanford.edu
if not os.path.exists(orig_data_file):
    print "Downloading data from the Stanford website (you must be connected to the internet)..."
    import urllib
    url = 'http://nlp.stanford.edu/data/glove.6B.zip'
    urllib.urlretrieve(url, orig_data_file)
    assert os.path.exists(orig_data_file), "Download of the data has failed"
    print "Success"

# Unzip data
if not os.path.exists(orig_data_file):
    print "Unzipping..."
    zip_ref = zipfile.ZipFile(orig_data_file, 'r')
    zip_ref.extractall(os.path.dirname(orig_data_file))
    zip_ref.close()
    print "Success"

# Read data from txt file
def read_data(file_path):
    """ Read a Gl
