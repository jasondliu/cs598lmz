import codecs
codecs.register_error("strict", codecs.ignore_errors)

def main():
	reload(sys)
	sys.setdefaultencoding("utf-8")
	queries_content = gzip.open("/mnt/storage/more/relevance_data/queries.txt.gz").read().decode("utf-8", "strict").encode("utf-8")
	queries = [q.strip().lower() for q in queries_content.split("\n") if len(q.strip()) > 0]

	alphabet = "abcdefghijklmnopqrstuvwxyz\t\n\r1234567890"
	char_to_int = dict((c, i) for i, c in enumerate(alphabet))
	int_to_char = dict((i, c) for i, c in enumerate(alphabet))

	vocab_size = len(alphabet)
	seq_length = 50

	print 'Total Queries: %d' % len(queries)

	X, y = [], []
	for q in queries:
