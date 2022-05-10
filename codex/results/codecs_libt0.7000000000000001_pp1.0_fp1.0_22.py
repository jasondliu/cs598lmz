import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)
from math import sqrt
from matplotlib import pyplot as plt
from collections import defaultdict
import json
from pathlib import Path
from lib.drdata import DRData
from lib.drdata.drdata import get_item
from pprint import pprint
from lib.drdata.drdata import DRData
from lib.drdata.drdata import get_item
from lib.gazetteer import Gazetteer
from lib.gazetteer.gazetteer import Gazetteer
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_paris
from lib.utils import get_
