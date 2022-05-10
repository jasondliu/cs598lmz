import bz2
bz2_file = bz2.BZ2File('./data/train_data.json.bz2')
train_data = json.load(bz2_file)
bz2_file.close()

bz2_file = bz2.BZ2File('./data/test_data.json.bz2')
test_data = json.load(bz2_file)
bz2_file.close()

train_data = np.array(train_data)
test_data = np.array(test_data)

print(train_data.shape)
print(test_data.shape)

import random
random.shuffle(train_data)

train_data_x = [train_data[i][0] for i in range(len(train_data))]
train_data_y = [train_data[i][1] for i in range(len(train_data))]

test_data_x = [test_data[i][0] for i in range(len(test_data))]
test_data
