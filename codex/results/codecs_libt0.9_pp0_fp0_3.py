import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def log_the_mess(mess, datasave):
    now = datetime.datetime.now()
    print('\n    Date : {}\n    Log Infos : {}'.format(now, mess))
    with open(datasave, 'r') as f:
        lines = f.readlines()
        f.close()

    lines.append(str(now) + ';' + mess + '\n')

    with open(datasave, 'w') as f:
        f.writelines(lines)
        f.close()

def get_classify(values, key):
    """
    :param values: is an ordered list of dictionnary of classification
            {'id_class' : (int) , 'desc_class' : str}
    :param key: str of desc_class to find
    :return: boolean if key is in values list
    """
    for value in values:
        if key == value['desc_class
