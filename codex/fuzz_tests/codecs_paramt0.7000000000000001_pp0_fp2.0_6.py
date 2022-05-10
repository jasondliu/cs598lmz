import codecs
codecs.register_error('replace_spaces', codecs.replace_errors(u' ', u' '))
# print(spacy.__version__)
# print(en_core_web_sm.__version__)
# print(en_core_web_sm.vocab.strings)
# print(en_core_web_sm.Defaults.stop_words)


class Utils(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all_file_paths(root_path):
        all_paths = []
        for (dir_path, dir_names, file_names) in walk(root_path):
            all_paths.extend(list(map(lambda x: join(dir_path, x), file_names)))
        return all_paths

    @staticmethod
    def get_all_dir_paths(root_path):
        all_paths = []
        for (dir_path, dir_names, file_names) in walk(root_path):
            all_paths.extend(list(map
