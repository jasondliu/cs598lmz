import ctypes
ctypes.cdll.LoadLibrary(r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin\cudart64_100.dll')

from torch.utils.data import Dataset


class Dataset(Dataset):
    def __init__(self, x, y):
        self.len = x.shape[0]
        self.x_data = torch.from_numpy(x)
        self.y_data = torch.from_numpy(y)

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


class Model(nn.Module):
    def __init__(self, in_size, h1, h2, out_size):
        super(Model, self).__init__()
        self.l1 = nn.Linear(in_size, h1)
        self.l2 = nn.Linear(h1, h2)
        self.l3
