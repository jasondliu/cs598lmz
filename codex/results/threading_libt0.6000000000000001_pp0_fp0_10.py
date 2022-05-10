import threading
threading.stack_size(67108864)

def main():
    if len(sys.argv) != 2:
        print("Usage: python test.py [path_to_dataset]")
        exit()

    # Load dataset
    path_to_dataset = sys.argv[1]
    dataset = load_dataset(path_to_dataset, task='img_qa')

    print("Building model...")
    model = ImgQAModel(dataset['vocab_size'], dataset['num_answers'])
    model.compile(optimizer='adam', loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train model
    print("Training model...")
    history = model.fit([dataset['image_features'], dataset['question_features']],
                        dataset['answers'], batch_size=32, epochs=100,
                        validation_split=0.1, verbose=2)

    # Save model
    print("Saving model...")

