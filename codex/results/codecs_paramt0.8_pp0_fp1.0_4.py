import codecs
codecs.register_error('replace_with_space', stringreplace.replace_with_space)


def get_file(the_file, mode):
    """
    Gets a file as a generator object

    :param the_file: the file to open
    :param mode: the mode to open the file
    :return: a file object
    """
    return codecs.open(filename=the_file, mode=mode, encoding='utf-8', errors='ignore')


def files_with_extension(directory, extension):
    """
    Gets a list of files with the specific extention in a folder

    :param directory: the directory to search
    :param extension: the extension to search
    :return: a list of files
    """
    return (each_file for each_file in os.listdir(directory) if each_file.endswith(extension))


def files_with_extension_in_sub_directories(directory, extension):
    """
    Gets a list of files with the specific extention in a folder and sub folders

    :param directory: the directory to search
    :param extension
