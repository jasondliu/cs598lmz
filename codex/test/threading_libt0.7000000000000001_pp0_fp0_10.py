import threading
threading.stack_size(2**28)

def get_data(path, label):
    image = cv2.imread(path, 0)
    image = cv2.resize(image, (100,100))
    return image, label

def get_dataset(batch_size, image_paths, labels):
    train_image_dataset = tf.data.Dataset.from_tensor_slices((image_paths, labels))
    train_image_dataset = train_image_dataset.map(get_data, num_parallel_calls=AUTOTUNE)
    train_image_dataset = train_image_dataset.batch(batch_size)
    train_image_dataset = train_image_dataset.prefetch(buffer_size=AUTOTUNE)
    return train_image_dataset

def read_images(images_path, images_names, labels):
    images_paths, images_labels = [], []
