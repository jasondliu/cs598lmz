import codecs
codecs.register_error('replace', lambda e: (u'?', e.start + 1))
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def tofloat(value):
    try:
        return float(value)
    except:
        return np.nan

def toint(value):
    try:
        return int(value)
    except:
        return np.nan

def load_data(path_file, usecols=[]):
    #usecols = [0, 1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 45, 46, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]
    data = pd.read_csv(path_file, usecol
