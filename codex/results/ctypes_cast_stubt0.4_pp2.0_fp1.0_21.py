import ctypes
ctypes.cast(0, ctypes.py_object).value

# Import modules from parent directory
import sys
sys.path.append('..')

from lib.utils import *

# Get the data
x_train, y_train, x_test, y_test = get_MNIST_data()

# Get the model
model = get_MNIST_model()

# Train the model
model.fit(x_train, y_train, batch_size=128, epochs=1)

# Evaluate the model
score = model.evaluate(x_test, y_test)

print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Save the model
save_model(model)
