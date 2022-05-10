import mmap
import os

from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsError
from kazoo.handlers.threading import SequentialThreadingHandler
from kazoo.recipe.watchers import ChildrenWatch, DataWatch

import sys
