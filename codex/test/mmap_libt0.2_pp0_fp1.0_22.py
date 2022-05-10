import mmap
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from functools import partial
from itertools import chain, groupby
from operator import attrgetter
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Union

