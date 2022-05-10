import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

list_queries = []
for line in sys.stdin:
	parts = line.replace('\n','').split('|')
	list_q = parts[0].split(' ')
	list_q = list(set([x for x in list_q if int(x) not in word_list]))
	list_queries.append((list_q, parts[1]))

n_feat = len(word_list)
temp_file = "tmp_feat_file"
test_feats = open(temp_file, "w")
for x in list_queries:
	feats = [0] * n_feat
	for w in x[0]:
		feats[word_list[int(w)]] = 1
	test_feats.write("%s\n" % feats)
test_feats.close()

data = np.loadtxt(open(temp_file,"rb"),delimiter=",")

