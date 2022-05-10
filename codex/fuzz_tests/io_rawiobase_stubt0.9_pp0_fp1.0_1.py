import io
class File(io.RawIOBase):
    """Base class for all files.
    This object should be used to access data in files. 
    You will never instantiate this class.

    Args:
        path (str) path of the file
        is_test (bool,optional): use in `TFRecordDataset` to 
            specify that this is the test split of the data.
    """

    def __init__(self, path, is_test):
        raise NotImplementedError("create your own File object")
        self.is_test = is_test

    def __iter__(self):
        """Iterate over the objects in the `File`.
        
        Yields:
            tf.data.Dataset object. Yield will stop when all samples
            in the file have been yielded.
        """
        raise NotImplementedError("implement this in your File class")

    def __len__(self):
        """Number of samples in the `File` object.
        """
        raise NotImplementedError("implement this in your File class")
        
    def __getitem__(self
