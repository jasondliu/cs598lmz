import codecs
codecs.register_error("strict", codecs.ignore_errors)

class CountLines:
    """
    count number of lines
    """
    def __init__(self):
        self.count = 0
        self.skip_intervals = [
            (0, 0), (0, 1), (1, 58), (2, 0), (2, 54), (2, 57),
            (3, 13), (3, 20), (3, 23), (3, 28), (3, 30), (3, 33), (3, 36), (3, 39),
            (3, 42), (3, 44), (3, 46), (3, 49), (3, 51), (3, 54), (3, 56), (3, 59),
            (4, 2), (4, 6), (4, 9), (4, 11), (4, 13), (4, 15), (4, 17), (4, 19),
            (4, 21), (4, 23), (4, 25), (4, 28), (4, 30), (4, 33), (4, 35), (4, 37),
