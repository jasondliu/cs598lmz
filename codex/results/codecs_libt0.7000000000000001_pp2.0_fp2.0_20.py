import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)
#import pdb; pdb.set_trace()

class EvReader:
    """
    Class to read data from the open-ephys ephys data format.
    """
    def __init__(self,filepath,group_index=0,channel_index=0,start_index=0,stop_index=0,chunksize=0,nchannels=0):
        """
        Constructor for the EvReader Class

        filepath: Path to a .ev file
        group_index: The index of the channel group to return data from.
        channel_index: The index of the channel within the channel group to return data from.
        start_index: The start index of the data to return.
        stop_index: The stop index of the data to return.
        chunksize: The size of the chunk to read in, if 0, all will be read.
        nchannels: The number of channels on the device.
        """
        self.filepath = filepath

