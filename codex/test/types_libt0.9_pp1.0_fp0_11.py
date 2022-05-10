import types
types.SimpleNamespace

import random
# import os
# print(os.getcwd())
# os.chdir('/Users/alex/workspace/speech-recognition-neural-network')

class Generator(object):
    def __init__(self, batch_size=64, input_shape=(161, 99, 1)):
        # The size of the batch that is propagated through the network 
        self.batch_size = batch_size
        self.input_shape = input_shape

    def generator(self):            
        while True:
            features = []
            targets = []
            for i in range(self.batch_size):
                # Get a random index to look up a feature/label pair
                index = np.random.randint(len(training_labels))

                # Preprocess the feature
                feature = training_features[index]
                feature = (feature - np.min(feature)) / (np.max(feature) - np.min(feature))
                feature = np.reshape(feature, self.input_shape)
                
                # Get
