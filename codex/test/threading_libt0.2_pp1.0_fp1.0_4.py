import threading
threading.stack_size(67108864)

def main():
    print("Starting")
    print("Loading data...")
    data = load_data()
    print("Data loaded")
    print("Creating model...")
    model = create_model(data)
    print("Model created")
    print("Training model...")
    train_model(model, data)
    print("Model trained")
    print("Saving model...")
    save_model(model)
    print("Model saved")
    print("Finished")

def load_data():
    data = {}
    data["train_x"] = np.load("data/train_x.npy")
    data["train_y"] = np.load("data/train_y.npy")
    data["val_x"] = np.load("data/val_x.npy")
    data["val_y"] = np.load("data/val_y.npy")
    data["test_x"] = np.load("data/test_x.npy")
    data["test_y"]
