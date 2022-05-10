import codecs
codecs.register_error('strict', codecs.lookup("ascii"))

def get_model_path(temp_path, model_name, version=None):
    """Get model path, by version or latest.

    Args:
        model_name (str): Model name, 'w2v' or 'classifier'.
        version (str, optional): Version number, latest if not provided.

    Returns:
        str: Model path.

    """
    latest_file = os.path.join(temp_path, model_name, 'LATEST')
    latest_version = open(latest_file, 'r').read().strip()
    if version is None:
        version = latest_version
    return os.path.join(temp_path, model_name, version)

class Classifier(object):
    """Classifier Class

    Args:
        model_path (str): Classifier model path.

    """
    def __init__(self, model_path):
        self.model = fasttext.load_model(model_path)

    def predict(self, sentence, k=
