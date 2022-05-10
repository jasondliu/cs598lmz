import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    # Read the data
    data = pd.read_csv("../../data/processed/train_data.csv", encoding="utf-8")
    data = data.sample(frac=1).reset_index(drop=True)
    data = data[:50]

    # Split into train and test
    train_data, test_data = train_test_split(data, test_size=0.2)

    # Create the model
    model = create_model()

    # Train the model
    model.fit(train_data["text"], train_data["label"], batch_size=10, epochs=5)

    # Evaluate the model
    result = model.evaluate(test_data["text"], test_data["label"])
    print(result)

    # Save the model
    model.save("../../models/model.h5")


def create_model():
    # Create the model
    model = Sequential()
    model.add(Embedding(10000, 64))
    model
