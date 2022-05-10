import ctypes
ctypes.cdll.LoadLibrary('./build/lib/libcaffe.so')
import caffe

dim = (3,224,224)

maxOuputLength = max([len(value) for value in codebook.values()])


training_materials = []

for fn in glob.glob('/home/ubuntu/meanwhile/images/*/*'):
  sys.stdout.write('.')
  sys.stdout.flush()
  label = fn[fn.find('images/')+7:].replace('/','_')
  if label not in codebook.values():
    continue
  data = np.load(fn).astype('float')
  input = np.zeros((dim[2],dim[2],dim[0],1))
  input[:,:,:,0] = data.transpose(2,0,1)[:,:,::-1]
  input -= np.array([104.0, 117.0, 123.0]).reshape(1,1,3)
  output = 256*np.ones((maxOuputLength,))

