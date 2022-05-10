import ctypes
ctypes.cast(address_as_int, ctypes.py_object).value

def get_memory_estimate(model):
    return get_label_memory(model.left) + get_label_memory(model.right)

estimate_memory(dt)

# Print the new tree estimated memory and compare it to the original
print(get_memory_estimate(dt))
print(get_memory_estimate(old_tree))

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict the labels of the training set
y_pred = dt.predict(X_train)

# Evaluate the training set accuracy of dt
accuracy = accuracy_score(y_train, y_pred)

# Print accuracy
print("Accuracy: {:.2f}".format(accuracy))

# Define the grid of values for max_depth:
depths = [2, 3, 5, 7, 9]

# Iterate over depths
grid_accuracy = []
for depth in depths:

    # Create a tree with max
