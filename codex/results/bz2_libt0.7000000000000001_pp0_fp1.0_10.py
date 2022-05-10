import bz2
bz2.decompress(compressed_data)

# open bzip2 file
bzip2_file = bz2.BZ2File('example.bz2')

# read bzip2 file
bzip2_file.read()

# close bzip2 file
bzip2_file.close()

#########

# Logging
import logging
logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')

# Logging to a file
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

#########

# Timing the execution of code
import timeit
timeit.timeit('"-".join(str(n) for n in range(100))
