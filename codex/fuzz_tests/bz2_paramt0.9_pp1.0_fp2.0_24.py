from bz2 import BZ2Decompressor
BZ2Decompressor

from tqdm import tqdm, tqdm_gui
tqdm.pandas(tqdm_gui)

import logging
logger = logging.getLogger()

from logging import StreamHandler
file_handler = StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#import jupyter notebook
from IPython.display import display, clear_output


import warnings
warnings.filterwarnings("ignore")

# Use seaborn style defaults and set the default figure size
sns.set(rc={'figure.figsize':(20, 10)})
temp_path = '../data/temp'

 
_comment = """
logging.INFO = 20
logging.DEBUG = 10

https://stackoverflow.com/questions/1378160/how-can-i-disable-the-logging-of-some-library-
