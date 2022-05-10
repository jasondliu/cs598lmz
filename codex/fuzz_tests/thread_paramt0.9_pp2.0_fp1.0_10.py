import sys, threading
threading.Thread(target=lambda: sys.stdout.write('.')).start()
sample1 = 'троллейбус' # also 'троллейбус'
sample2 = 'аутлайн' # also 'аутлайн'

sample1_str2idx = list(map(lambda tkn: tkn2idx[tkn], [sample1[:i] for i in range(1, len(sample1))] + [sample1]))
sample2_str2idx = list(map(lambda tkn: tkn2idx[tkn], [sample2[:i] for i in range(1, len(sample2))] + [sample2]))

del sample1_str2idx[4]
del sample1_str2idx[4]
del sample1_str2idx[4]
del sample1_str2idx[4]
del sample1_str2idx[4]

del sample2_str2idx[2]
del sample2_
