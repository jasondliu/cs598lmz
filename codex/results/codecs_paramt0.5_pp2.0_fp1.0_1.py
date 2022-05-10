import codecs
codecs.register_error('surrogate_escape', codecs.backslashreplace)

def get_data_from_xml(path):
    """
    :param path: path to the xml file
    :return: xml data
    """
    with codecs.open(path, 'r', 'utf-8', 'surrogateescape') as f:
        xml_data = f.read()

    return xml_data


def get_data_from_json(path):
    """
    :param path: path to the json file
    :return: json data
    """
    with codecs.open(path, 'r', 'utf-8', 'surrogateescape') as f:
        json_data = json.load(f)

    return json_data


def get_data_from_csv(path):
    """
    :param path: path to the csv file
    :return: csv data
    """
    with codecs.open(path, 'r', 'utf-8', 'surrogateescape') as f:
        csv_data = f.readlines()


