import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def my_callback(arg1, arg2):
    print("my_callback was called with %d, %d" % (arg1, arg2))
    return 0
CALLBACK = FUNTYPE(my_callback)

# Initialize the library with the API key
# found in your dashboard.
libmetrc.initialize("API_KEY")

# Create a new plant batch
plant_batch = libmetrc.PlantBatch.create(
    "2018-02-01",
    "Flower",
    "abc123",
    "Plant A",
    2,
    "grams",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
    "Plant Room 1",
   
