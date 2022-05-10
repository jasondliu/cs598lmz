import threading
threading.stack_size(1000000)
from StreamDirectory import StreamDirectory
from CreateDatabase import CreateDatabase
from CleanDatabase import CleanDatabase
from CleanTables import CleanTables
from Program import Program
from CreateTables import CreateTables
from CreateProcs import CreateProcs
from RunProcs import RunProcs
from QueryDatabase import QueryDatabase
from LoadBalancer import LoadBalancer
from DropDatabase import DropDatabase
from DropTables import DropTables
from DropProcs import DropProcs
from AggregateTables import AggregateTables

'''
# TODO: Investigate performance issues with loading a directory of the same data.
# Determine if the process is I/O bound. Directories
# can be a bit trickier.
# TODO: When you kill RDBMS, does it kill Python as well?
# TODO: Remove unnecessary imports (e.g. subprocess).
# TODO: Investigate PythonRocksDB.
# TODO: Identify easy optimizations.
# TODO: Look into and benchmark the major advantages of Pytorch.
'''

# Easily change the location and names
