from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(records[20])

def read_bz2_file(file):
    file_open = bz2.open(file, 'rt')
    data = []
    for line in file_open:
        data.append(line)
    file_open.close()
    return data

read_bz2_file(os.path.join(path,'stackoverflow.com-Posts.7z.001'))

sample_file = os.path.join(path, 'stackoverflow.com-Posts.7z.001')

# This method reads in a file and returns a list of dictionaries.  Each item in the list
# corresponds to a post on StackOverflow.  Each dictionary contains the following information:
# - body: the text of the question
# - title: the title of the question
# - tag: the tags given to the question (only one tag per question)
# - id: the unique identifier of the question

# Your task is to complete the body of the function.  The starter code reads
# some of the data in, and you need to
