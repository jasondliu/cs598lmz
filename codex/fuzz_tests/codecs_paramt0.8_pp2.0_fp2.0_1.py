import codecs
codecs.register_error('replace_space', ReplacedSpaceEncoder)
 
# Define the dataset class
class Seq2SeqDataset(Dataset):
	def __init__(self, src_wrd2id, tgt_wrd2id, src_file, tgt_file):
		self.src_wrd2id = src_wrd2id
		self.tgt_wrd2id = tgt_wrd2id

		self.src_data = open(src_file, 'r').readlines()
		self.tgt_data = open(tgt_file, 'r').readlines()

	def __len__(self):
		return len(self.src_data)

	def __getitem__(self, idx):
		src_seq = self.src_data[idx].split()
		tgt_seq = self.tgt_data[idx].split()

		src_id_seq = [self.src_wrd2id[w] if w in self.src_wrd2id else self
