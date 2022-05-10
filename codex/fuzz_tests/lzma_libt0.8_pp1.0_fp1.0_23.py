import lzma
lzma.LZMADecompressor().decompress(meta)

meta_json = json.loads(meta)

for i in meta_json['datasets']:
    if i['dataset_name'] == 'test':
        test_meta = i

test_meta


test_meta['start']
test_meta['end']
test_meta['counts_per_image']

1 + (test_meta['end'] - test_meta['start']) // test_meta['counts_per_image']


from collections import Counter
Counter([c//test_meta['counts_per_image'] for c in test_meta['labels']])

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
unlabeled_X_train, X_val, unlabeled_y_train, y_val = train_test_split(
    dataset_meta['X_train'][:10000], dataset_meta['y_train'][:10000], test_size=5000)

X_train, X_
