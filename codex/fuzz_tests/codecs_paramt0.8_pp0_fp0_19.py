import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)
csv.field_size_limit(sys.maxsize)

from collections import defaultdict
from collections import Counter
import re
import pickle
#from gensim import corpora, models, similarities

# Loads the CSV file into a list of lists
#skips the first row
def load_csv(file_name):
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        next(reader)
        list_of_lists = [row for row in reader]
    return list_of_lists

#Creates a dictionary with key = blockid, value = crime
def blockid_crime_dict(file_name):
    list_of_lists = load_csv(file_name)
    block_id_crime_dict = {blockid[14]:crime for blockid, crime in list_of_lists}
    return block_id_crime_dict

#Creates a dictionary with key = blockid, value = crimes
