import threading
threading.stack_size(2**27)

class Train(threading.Thread):
    def __init__(self, threadID, name, count, model):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.count = count
        self.model = model

    def run(self):
        print("Starting " + self.name)
        train_model(self.model, self.name, self.count)
        print("Exiting " + self.name)

def create_model(n_hidden, n_layers):

    model = Sequential()
    model.add(LSTM(
            n_hidden,
            input_shape=(1, 1),
            return_sequences=True))
    for i in range(n_layers - 1):
        model.add(LSTM(n_hidden, return_sequences=True))
    model.add(TimeDistributed(Dense(1)))
