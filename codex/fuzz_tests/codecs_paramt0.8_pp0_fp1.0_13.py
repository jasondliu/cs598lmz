import codecs
codecs.register_error('replace_with_space', codecs.replace_with_spaces)
import sys
#import dill

#--------------------------------------------------------------------------------------------------#
#                                            General Config                                         #
#--------------------------------------------------------------------------------------------------#
data_path = str(sys.argv[1]) #"../data/"
tweet_type = str(sys.argv[2]) #"tweet"
embedding_type = str(sys.argv[3]) #"GloVe"
embedding_size = int(sys.argv[4]) #300
embedding_layer = str(sys.argv[5]) #"embedding"
hidden_size = int(sys.argv[6]) #512
first_bidirectional = True
second_bidirectional = False
model_type = "recurrent"
rnn_type = "lstm"
cell_size = int(sys.argv[7]) #"256"
loss_function = nn.CrossEntropyLoss()
lr = float(sys.argv[8]) #0.001
epochs_number = int(sys.
