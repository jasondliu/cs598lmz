import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# for i in range(10):
#     m = view[i].numpy()
#     print(m)
#     print(np.shape(m), m.dtype)

# print(np.shape(view), view.dtype)
# way too slow
# def ArrayToTensor(np_arr):
#     tensor = torch.from_numpy(np_arr)
#     if np.isfortran(np_arr):
#         tensor = tensor.contiguous()
#     return tensor

model = torch.jit.load('test_pt.pt')

test_dataset = torchvision.datasets.LSUN(root='lsun', classes=['test'], transform=transforms.ToTensor())
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=1, shuffle=True, num_workers=4)
test_iter = iter(test_dataloader)
test_input = torch.unsqueeze(test_iter.next()[0],
