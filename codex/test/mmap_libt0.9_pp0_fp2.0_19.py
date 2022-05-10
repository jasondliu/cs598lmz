import mmap

COLOR_BLACK = '\u001b[30m'
COLOR_RED = '\u001b[31m'
COLOR_GREEN = '\u001b[32m'
COLOR_YELLOW = '\u001b[33m'
COLOR_BLUE = '\u001b[34m'
COLOR_MAGNETA = '\u001b[35m'
COLOR_CYAN = '\u001b[36m'
COLOR_WHITE = '\u001b[37m'
COLOR_RESET = '\u001b[0m'


def isColorEnabled(test_function):
    """
    文字色出力を有効にするためのデコレータ
    :param test_function: テスト関数
    :return: テスト関数
    """

