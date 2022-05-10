import threading
threading.stack_size(2**27) #threading.Thread(target=main).start()
'''
def test_run():
    start = time.time()
    print("preparing the test")
    trn_df = pd.read_csv('../input/train.csv')
    #sub_df = pd.read_csv('../input/sample_submission.csv')
    #sub_df["target"] = np.random.rand(sub_df.shape[0])
    #sub_df.to_csv("submission.csv", index=False)
    print("time for test: %.2f" % (time.time() - start))
 
#test_run()
'''

# reading data
train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

# shape
print('Shape train: {}\nShape test: {}'.format(train.shape, test.shape))

y_train=train['target']
