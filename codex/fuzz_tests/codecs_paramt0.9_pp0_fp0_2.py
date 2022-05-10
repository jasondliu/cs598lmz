import codecs
codecs.register_error('error', codecs.ignore_errors)

# %%
# обработка отдельного результата вопроса
qid_to_data = defaultdict(list)
for line in open(Qid_data_path + 'qid_data.txt', encoding="cp1251"):
    qid, data = line.strip().split('\t', 1)
    qid_to_data[qid].append(data)

# %%
# обработка отдельного результата тренировочного датасета
for line in open(Yr_data_path + 'train_data.txt', encoding="cp1251"):
    qid, data = line.strip().split('\t', 1)
    qid_to_data[qid
