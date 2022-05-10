import mmap, os, sys

# print 'sys.argv[0] =', sys.argv[0]

# LISTING_FILE = sys.argv[1]
# DATABASE_FILE = sys.argv[2]

LISTING_FILE = '../data/listings20160229.txt'
DATABASE_FILE = '../data/database.txt'


def parse_query(line):
    '''
    Parses a query of the format
    "QUERY <query_id> <query_type> <query_parameter>".

    Returns a tuple of the form (query_id, query_type, query_parameter).
    '''
    parts = line.split()
    return int(parts[1]), parts[2], parts[3]

def process_query(query):
    '''
    Runs a query against the database file.
    '''
    query_id, query_type, query_parameter = query

