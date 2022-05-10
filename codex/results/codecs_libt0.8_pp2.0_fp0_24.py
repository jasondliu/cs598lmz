import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# Global objects
scores = {}

# File paths
path = './data/'
db_path = path + '1-movies-db.txt'
db_cut_path = path + '1-movies-db-cut.txt'
db_cut_query_path = path + '1-movies-db-cut-query.txt'
db_cut_query_scores_path = path + '1-movies-db-cut-query-scores.txt'
db_cut_query_scores_sorted_path = path + '1-movies-db-cut-query-scores-sorted.txt'

# Parameters
clusters = 10
queries = 10
epochs = 10
keep_prob = 0.5
batch_size = 32

def read_db_cut_query():
    movies_query = []
    with open(db_cut_query_path, encoding='utf-8', mode='r
