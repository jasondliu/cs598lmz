import _struct
import matplotlib.pyplot as plt
from numpy import array

def get_split_index(percent,line_nums):
    split_index = []
    for i in percent:
        split_index.append(int(i/100.0*line_nums/len(percent))*len(percent))
    split_index = array(split_index)+[len(percent)*line_nums-1,0]
    split_index[-1] = -(len(percent)*-split_index[-1])
    split_index = sorted(split_index)
    print split_index
    return split_index

def read_image_2_array(filename):
    with open(filename,"r") as fp:
        read = np.fromfile(fp,np.uint8)
        print read[0]
        return read

def read_label_2_array(filename):
    with open(filename,"r") as fp:
        return np.fromfile(fp,np.uint8)

def shuffle_array(array_list
