import bz2
bz2_obj = bz2.BZ2File('data.bin.bz2')

'''
@parameter:
    numpy.ndarray shape=(243,32)
'''
def my_test(test):
    #print(test)
    data = numpy.frombuffer(test, numpy.uint8)
    #print(data)
    #print(len(data))
    # data are organized as (height, width, channel)
    #print(data.shape)
    #print(len(data))
    #print(type(data))
    #assert(data.shape == (243,32))

    # data are organized as (height, width, channel)
    #data = numpy.reshape(data, (243, 32))
    #data = numpy.transpose(data, (1, 0))
    #print(data.shape)

    data = numpy.reshape(data, (1, 243, 32, 1))
    data = torch.Tensor(data)
    data = data.cuda()

    # data - n
