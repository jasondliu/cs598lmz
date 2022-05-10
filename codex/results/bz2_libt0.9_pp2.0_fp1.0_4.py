import bz2
bz2_file_path = "mnist.pkl.bz2"
with bz2.open(bz2_file_path, "rb") as f:
    train_set, validation_set, test_set = pickle.load(f, encoding="bytes")
print("Training Set")
print("Number of Examples:\t",len(train_set[0]))
print("Size of an Example:\t",train_set[0][0].shape)
print("Number of Classes:\t",len(set(train_set[1])))
print("Type of Example:\t\t",type(train_set[0][0]))
print("Type of Labels:\t\t",type(train_set[1][0]))

print("\nValidation Set")
print("Number of Examples:\t",len(validation_set[0]))
print("Size of an Example:\t",validation_set[0][0].shape)
print("Number of Classes:\t",len(set(validation_set[1])))
print("Type of Example:\t\t",type
